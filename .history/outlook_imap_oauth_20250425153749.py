import imaplib
import email
import email.header
import sys
import base64
import json
import re
import html
import getpass
import webbrowser
import http.server
import socketserver
import urllib.parse
import threading
import secrets
import requests
from email.policy import default

# 全局变量，存储授权结果
auth_code = None
auth_completed = threading.Event()

class AuthHandler(http.server.SimpleHTTPRequestHandler):
    """处理OAuth重定向的HTTP服务器处理程序"""
    
    def do_GET(self):
        global auth_code
        
        # 解析URL查询参数
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        
        if "code" in params:
            # 如果URL包含授权码
            auth_code = params["code"][0]
            
            # 返回成功页面
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            response = """
            <html>
            <head><title>授权成功</title></head>
            <body>
            <h1>授权成功!</h1>
            <p>您已成功授权应用访问您的Outlook邮箱。可以关闭此窗口并返回程序。</p>
            </body>
            </html>
            """
            self.wfile.write(response.encode())
            
            # 通知主线程授权已完成
            auth_completed.set()
            
        else:
            # 如果没有授权码，返回错误
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            response = """
            <html>
            <head><title>授权失败</title></head>
            <body>
            <h1>授权失败</h1>
            <p>未能获取授权码。请重试。</p>
            </body>
            </html>
            """
            self.wfile.write(response.encode())

    def log_message(self, format, *args):
        # 禁止HTTP服务器日志输出，保持控制台整洁
        return

def get_authorization_code(client_id, redirect_uri, scopes):
    """获取OAuth2授权码"""
    # 创建一个随机的状态值，以防CSRF攻击
    state = base64.urlsafe_b64encode(secrets.token_bytes(32)).decode().rstrip("=")
    
    # 构造授权URL
    auth_url = (
        f"https://login.microsoftonline.com/common/oauth2/v2.0/authorize"
        f"?client_id={client_id}"
        f"&response_type=code"
        f"&redirect_uri={urllib.parse.quote(redirect_uri)}"
        f"&response_mode=query"
        f"&scope={urllib.parse.quote(scopes)}"
        f"&state={state}"
    )
    
    print(f"请在浏览器中访问以下URL，并完成授权:\n{auth_url}")
    
    # 打开浏览器进行授权
    webbrowser.open(auth_url)
    
    # 启动一个本地服务器来接收重定向
    server_address = urllib.parse.urlparse(redirect_uri).netloc.split(":")
    host = server_address[0]
    port = int(server_address[1]) if len(server_address) > 1 else 8000
    
    server = socketserver.TCPServer((host, port), AuthHandler)
    
    print(f"正在本地 {redirect_uri} 等待授权回调...")
    
    # 在单独的线程中运行服务器
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    
    # 等待授权完成或超时
    auth_completed.wait(timeout=300)  # 等待最多5分钟
    
    # 停止服务器
    server.shutdown()
    server.server_close()
    
    if not auth_code:
        print("授权失败或超时")
        return None
    
    print("成功获取授权码")
    return auth_code

def get_access_token(client_id, client_secret, code, redirect_uri):
    """使用授权码获取访问令牌"""
    token_url = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
    
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"
    }
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    print("正在获取访问令牌...")
    
    try:
        response = requests.post(token_url, data=data, headers=headers)
        response.raise_for_status()
        token_data = response.json()
        
        print("成功获取访问令牌")
        
        # 保存令牌到文件
        with open("outlook_oauth_tokens.json", "w") as f:
            json.dump(token_data, f, indent=4)
        print("令牌已保存到 outlook_oauth_tokens.json 文件")
        
        return token_data
    except Exception as e:
        print(f"获取令牌失败: {str(e)}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"错误详情: {e.response.text}")
        return None

def refresh_access_token(client_id, client_secret, refresh_token):
    """刷新访问令牌"""
    token_url = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
    
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    print("正在刷新访问令牌...")
    
    try:
        response = requests.post(token_url, data=data, headers=headers)
        response.raise_for_status()
        token_data = response.json()
        
        print("成功刷新访问令牌")
        
        # 更新令牌文件
        with open("outlook_oauth_tokens.json", "w") as f:
            json.dump(token_data, f, indent=4)
        print("令牌已更新并保存到 outlook_oauth_tokens.json 文件")
        
        return token_data
    except Exception as e:
        print(f"刷新令牌失败: {str(e)}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"错误详情: {e.response.text}")
        return None

def generate_oauth2_string(username, access_token):
    """生成IMAP OAuth2认证字符串"""
    auth_string = f"user={username}\x01auth=Bearer {access_token}\x01\x01"
    return base64.b64encode(auth_string.encode()).decode()

def get_email_with_oauth(username, access_token, mark_as_read=False):
    """使用OAuth访问令牌通过IMAP获取邮件"""
    # Outlook IMAP服务器设置
    imap_server = "outlook.office365.com"
    imap_port = 993
    
    print(f"正在连接到 {imap_server}...")
    
    try:
        # 连接到IMAP服务器
        mail = imaplib.IMAP4_SSL(imap_server, imap_port)
        
        # 使用OAuth2进行认证
        print(f"正在以 {username} 身份使用OAuth认证...")
        auth_string = generate_oauth2_string(username, access_token)
        mail.authenticate('XOAUTH2', lambda x: auth_string)
        print("OAuth认证成功！")
        
        # 选择收件箱
        print("正在访问收件箱...")
        mail.select("INBOX")
        
        # 搜索所有邮件
        print("正在搜索邮件...")
        result, data = mail.search(None, "ALL")
        
        if result != "OK" or not data[0]:
            print("未找到任何邮件")
            mail.logout()
            return None
        
        # 获取最新邮件的ID
        latest_email_id = data[0].split()[-1]
        
        # 提取邮件内容
        print(f"正在获取邮件 ID: {latest_email_id.decode()}...")
        result, data = mail.fetch(latest_email_id, "(RFC822)")
        
        if result != "OK":
            print(f"获取邮件失败: {result}")
            mail.logout()
            return None
        
        # 解析邮件内容
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email, policy=default)
        
        # 如果需要，标记为已读
        if mark_as_read:
            mail.store(latest_email_id, '+FLAGS', '\\Seen')
            print("已将邮件标记为已读")
        
        # 提取邮件信息
        subject = decode_header(email_message["Subject"])
        from_addr = decode_header(email_message["From"])
        date = email_message["Date"]
        
        # 提取邮件正文
        body = ""
        if email_message.is_multipart():
            for part in email_message.iter_parts():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))
                
                # 跳过附件
                if "attachment" in content_disposition:
                    continue
                
                # 获取文本内容
                if content_type == "text/plain":
                    body = part.get_payload(decode=True).decode('utf-8', errors='replace')
                    break
                elif content_type == "text/html" and not body:
                    html_body = part.get_payload(decode=True).decode('utf-8', errors='replace')
                    body = html_to_text(html_body)
        else:
            # 不是多部分邮件
            content_type = email_message.get_content_type()
            if content_type == "text/plain":
                body = email_message.get_payload(decode=True).decode('utf-8', errors='replace')
            elif content_type == "text/html":
                html_body = email_message.get_payload(decode=True).decode('utf-8', errors='replace')
                body = html_to_text(html_body)
        
        # 登出
        mail.logout()
        print("已成功从IMAP服务器登出")
        
        # 返回结果
        return {
            "id": latest_email_id.decode(),
            "subject": subject,
            "from": from_addr,
            "date": date,
            "body": body,
            "body_preview": body[:200] + "..." if len(body) > 200 else body
        }
    
    except imaplib.IMAP4.error as e:
        print(f"IMAP错误: {str(e)}")
        return None
    except Exception as e:
        print(f"发生错误: {str(e)}")
        import traceback
        print(traceback.format_exc())
        return None

def decode_header(header_value):
    """解码邮件头信息"""
    if not header_value:
        return "未知"
    
    decoded_header = email.header.decode_header(header_value)
    header_parts = []
    
    for value, charset in decoded_header:
        if isinstance(value, bytes):
            try:
                if charset:
                    header_parts.append(value.decode(charset))
                else:
                    header_parts.append(value.decode('utf-8', errors='replace'))
            except:
                header_parts.append(value.decode('utf-8', errors='replace'))
        else:
            header_parts.append(str(value))
    
    return ''.join(header_parts)

def html_to_text(html_content):
    """将HTML内容转换为纯文本"""
    # 删除HTML标签
    text = re.sub('<[^<]+?>', ' ', html_content)
    # 解码HTML实体
    text = html.unescape(text)
    # 去除多余空格
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def load_tokens():
    """从文件加载令牌"""
    try:
        with open("outlook_oauth_tokens.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        print("令牌文件格式错误")
        return None

def main():
    """主函数"""
    print("===== Outlook OAuth IMAP邮件获取程序 =====\n")
    
    # 客户端配置
    client_id = "9e5f94bc-e8a4-4e73-b8be-63364c29d753"  # 替换为您的应用ID
    client_secret = ""  # 替换为您的应用密钥（如果需要）
    redirect_uri = "https://localhost"
    scopes = "offline_access https://outlook.office.com/IMAP.AccessAsUser.All"
    
    # 检查是否已有令牌
    token_data = load_tokens()
    access_token = None
    refresh_token = None
    username = None
    
    if token_data and "access_token" in token_data:
        print("已从文件加载令牌")
        access_token = token_data.get("access_token")
        refresh_token = token_data.get("refresh_token")
        
        # 提示输入用户名
        username = input("请输入您的Outlook邮箱地址: ")
    else:
        # 如果没有令牌，获取新令牌
        username = input("请输入您的Outlook邮箱地址: ")
        
        # 获取授权码
        auth_code = get_authorization_code(client_id, redirect_uri, scopes)
        if not auth_code:
            print("获取授权码失败，程序退出")
            sys.exit(1)
        
        # 使用授权码获取令牌
        token_data = get_access_token(client_id, client_secret, auth_code, redirect_uri)
        if not token_data or "access_token" not in token_data:
            print("获取访问令牌失败，程序退出")
            sys.exit(1)
        
        access_token = token_data["access_token"]
        refresh_token = token_data.get("refresh_token")
    
    # 确认是否标记为已读
    mark_as_read_input = input("是否将邮件标记为已读? (y/n): ").lower()
    mark_as_read = mark_as_read_input in ('y', 'yes', 'true', 't', '1')
    
    # 获取邮件
    email_data = get_email_with_oauth(username, access_token, mark_as_read)
    
    # 如果失败且有刷新令牌，尝试刷新令牌
    if not email_data and refresh_token:
        print("使用访问令牌失败，尝试刷新令牌...")
        token_data = refresh_access_token(client_id, client_secret, refresh_token)
        if token_data and "access_token" in token_data:
            access_token = token_data["access_token"]
            print("使用刷新的令牌重试...")
            email_data = get_email_with_oauth(username, access_token, mark_as_read)
    
    if email_data:
        print("\n===== 邮件详情 =====")
        print(f"ID: {email_data['id']}")
        print(f"主题: {email_data['subject']}")
        print(f"发件人: {email_data['from']}")
        print(f"日期: {email_data['date']}")
        
        print("\n----- 邮件内容预览 -----")
        print(email_data['body_preview'])
        
        print("\n----- 完整邮件内容 -----")
        print(email_data['body'])
    else:
        print("\n无法获取邮件")

if __name__ == "__main__":
    main() 