import imaplib
import email
import email.header
import sys
import base64
import json
import re
import html
import requests
from email.policy import default

def refresh_access_token(client_id, refresh_token):
    """刷新访问令牌"""
    token_url = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
    
    data = {
        "client_id": client_id,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
        "scope": "offline_access https://outlook.office.com/IMAP.AccessAsUser.All"
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
        
        # 保存新的刷新令牌，以便下次使用
        if "refresh_token" in token_data:
            print(f"获取到新的刷新令牌: {token_data['refresh_token']}")
        
        return token_data.get("access_token")
    except Exception as e:
        print(f"刷新令牌失败: {str(e)}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"错误详情: {e.response.text}")
        return None

def generate_oauth2_string(username, access_token):
    """生成IMAP OAuth2认证字符串"""
    return f"user={username}\x01auth=Bearer {access_token}\x01\x01"
    # return base64.b64encode(auth_string.encode()).decode()

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

def get_email_with_password(username, password, mark_as_read=False):
    """使用密码通过IMAP获取邮件（备用方法）"""
    # Outlook IMAP服务器设置
    imap_server = "outlook.office365.com"
    imap_port = 993
    
    print(f"正在连接到 {imap_server}...")
    
    try:
        # 连接到IMAP服务器
        mail = imaplib.IMAP4_SSL(imap_server, imap_port)
        
        # 使用密码登录
        print(f"正在以 {username} 身份使用密码登录...")
        mail.login(username, password)
        print("密码登录成功！")
        
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


def get_verification_code(username, client_id, refresh_token):
    """获取邮件中的验证码
    Args:
        username: Outlook邮箱地址
        client_id: 应用ID
        refresh_token: 刷新令牌
    Returns:
        str: 6位数字验证码,未找到则返回None
    """
    mark_as_read = False
    
    # 尝试使用OAuth方式
    print("尝试使用OAuth方式获取邮件...")
    
    # 刷新访问令牌
    access_token = refresh_access_token(client_id, refresh_token)
    print(f"得到access_token: {access_token}")
    
    if access_token:
        # 使用访问令牌获取邮件
        email_data = get_email_with_oauth(username, access_token, mark_as_read)
        print("\n----- 完整邮件内容 -----")
        print(email_data['body'])
        if email_data:
            print("\n使用OAuth方式成功获取邮件！")
            
            # 从邮件内容中提取6位数字验证码
            code_match = re.search(r'\b\d{6}\b', email_data['body'])
            if code_match:
                verification_code = code_match.group()
                print(f"\n找到6位数字验证码: {verification_code}")
                return verification_code
            else:
                print("\n未找到6位数字验证码")
                return None
    
    return None

def main():
    """主函数"""
    print("===== Outlook 邮件获取程序 =====\n")
    
    # 固定参数配置 - 请替换为您的实际信息
    username = "FrancoWilliam4481@outlook.com"  # 替换为您的Outlook邮箱地址
    password = "gmcm98022"  # 替换为您的密码
    client_id = "9e5f94bc-e8a4-4e73-b8be-63364c29d753"  # 替换为您的应用ID
    refresh_token = "M.C557_BAY.0.U.-ClPTPu1BowsZ3N8YLlG6GqXw2mqLL!Xta61cPNjaHSuB7UgJpx8AwE5X4V3YDdb6t2NE0AjiqOSmCMUtRVRzHLZNbQGLHAUNiTWiXC!oK4A1za8aiXj6wrK9IfI9FWf6YuNe2ExEVPlx7p!3HggfIQ47tJgBwnlDlAJwWKHWue7tfVMGVpWNai3wz!5SvhV0LteuUaV*BdJyN*iSnW7G8AMMO97HO7DQHaTAArQITaqzpisulYPs!W1w!4UhWI0h0dJ5AAlLwFsoR5aKikQ2n1mgE4lBIXVi2rddqOczOzvjrkCA77dh30hZ59wuXvieu0EwZSfWJC9rvMZklVCq*BTHb8vkCvLHuyoEKDuT4P8KWmZOtjfC*jGH5s*JS*6JPYrq5KUmUFCFwCDSbvu2ReMR3uYMuUOxOmNwuNWI2b6t"  # 替换为您的刷新令牌
    mark_as_read = False  # 是否将邮件标记为已读
    
    # 第一种方法：尝试使用OAuth方式
    print("尝试使用OAuth方式获取邮件...")
    
    # 刷新访问令牌
    access_token = refresh_access_token(client_id, refresh_token)
    print(f"得到access_token: {access_token}")
    if access_token:
        # 使用访问令牌获取邮件
        email_data = get_email_with_oauth(username, access_token, mark_as_read)
        
        if email_data:
            print("\n使用OAuth方式成功获取邮件！")
            
            print("\n===== 邮件详情 =====")
            print(f"ID: {email_data['id']}")
            print(f"主题: {email_data['subject']}")
            print(f"发件人: {email_data['from']}")
            print(f"日期: {email_data['date']}")
            
            print("\n----- 邮件内容预览 -----")
            print(email_data['body_preview'])
            
            print("\n----- 完整邮件内容 -----")
            print(email_data['body'])
            # 从邮件内容中提取6位数字验证码
            verification_code = None
            code_match = re.search(r'\b\d{6}\b', email_data['body'])
            if code_match:
                verification_code = code_match.group()
                print("\n----- 验证码 -----") 
                print(f"找到6位数字验证码: {verification_code}")
            else:
                print("\n未找到6位数字验证码")
            
            # 退出程序
            sys.exit(0)
    
    # 第二种方法：尝试使用密码方式（如果OAuth方式失败）
    # print("\n尝试使用密码方式获取邮件...")
    # email_data = get_email_with_password(username, password, mark_as_read)
    
    # if email_data:
    #     print("\n使用密码方式成功获取邮件！")
        
    #     print("\n===== 邮件详情 =====")
    #     print(f"ID: {email_data['id']}")
    #     print(f"主题: {email_data['subject']}")
    #     print(f"发件人: {email_data['from']}")
    #     print(f"日期: {email_data['date']}")
        
    #     print("\n----- 邮件内容预览 -----")
    #     print(email_data['body_preview'])
        
    #     print("\n----- 完整邮件内容 -----")
    #     print(email_data['body'])
    # else:
    #     print("\n两种方式都无法获取邮件，请检查账号信息或网络连接。")

if __name__ == "__main__":
    main() 