import requests
import webbrowser
import http.server
import socketserver
import urllib.parse
import json
import time
import threading
import base64
import secrets

# 需要用户填写的信息
CLIENT_ID = "db3127ee-cc97-4566-bdd7-0b22bb5b7968"  # 在Azure Portal应用注册中获取
REDIRECT_URI = "http://localhost:8000"
SCOPES = "Mail.Read offline_access"  # 离线访问和邮件读取权限

# 存储授权结果
auth_code = None
auth_completed = threading.Event()

class AuthHandler(http.server.SimpleHTTPRequestHandler):
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

def get_tokens(code):
    """使用授权码获取访问令牌和刷新令牌"""
    token_url = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
    
    data = {
        "client_id": CLIENT_ID,
        "scope": SCOPES,
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code"
    }
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    response = requests.post(token_url, data=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"获取令牌失败: {response.status_code} - {response.text}")
        return None

def main():
    global auth_code
    
    # 验证配置
    if not CLIENT_ID:
        print("错误: 请先设置CLIENT_ID")
        return
    
    # 创建一个随机的状态值，以防CSRF攻击
    state = base64.urlsafe_b64encode(secrets.token_bytes(32)).decode().rstrip("=")
    
    # 构造授权URL
    auth_url = f"https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={urllib.parse.quote(REDIRECT_URI)}&response_mode=query&scope={urllib.parse.quote(SCOPES)}&state={state}"
    
    print(f"请在浏览器中访问以下URL，并完成授权:\n{auth_url}")
    
    # 打开浏览器进行授权
    webbrowser.open(auth_url)
    
    # 启动一个本地服务器来接收重定向
    server = socketserver.TCPServer(("", 8000), AuthHandler)
    
    print("等待授权完成...")
    
    # 在单独的线程中运行服务器
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    
    # 等待授权完成
    auth_completed.wait(timeout=300)  # 等待最多5分钟
    
    # 停止服务器
    server.shutdown()
    
    if not auth_code:
        print("授权失败或超时")
        return
    
    print("授权成功，正在获取令牌...")
    
    # 使用授权码获取令牌
    tokens = get_tokens(auth_code)
    
    if tokens:
        print("\n===== 令牌信息 =====")
        print(f"访问令牌: {tokens.get('access_token', '(未获取)')[:30]}...")
        print(f"刷新令牌: {tokens.get('refresh_token', '(未获取)')}")
        print(f"过期时间: {tokens.get('expires_in', '(未知)')} 秒")
        
        # 将令牌保存到文件
        with open("outlook_tokens.json", "w") as f:
            json.dump(tokens, f, indent=4)
        
        print("\n令牌已保存到 outlook_tokens.json 文件中")
        print("\n请使用获取到的刷新令牌更新您的脚本")
    else:
        print("获取令牌失败")

if __name__ == "__main__":
    print("===== Microsoft OAuth2授权工具 =====")
    print("本工具将帮助您获取新的刷新令牌\n")
    
    main() 