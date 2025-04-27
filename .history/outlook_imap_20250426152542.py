import imaplib
import email
import email.header
import sys
from email.policy import default
import getpass
import html
import re

def get_first_email_imap(username, password, mark_as_read=False):
    """
    使用IMAP协议获取Outlook邮箱中的第一封邮件
    
    参数:
        username (str): Outlook邮箱地址
        password (str): 邮箱密码
        mark_as_read (bool): 是否将邮件标记为已读
        
    返回:
        dict: 包含邮件详细信息的字典，如果失败则返回None
    """
    # Outlook IMAP服务器
    imap_server = "outlook.office365.com"
    imap_port = 993
    
    print(f"正在连接到 {imap_server}...")
    
    try:
        # 连接到IMAP服务器
        mail = imaplib.IMAP4_SSL(imap_server, imap_port)
        
        # 登录
        print(f"正在以 {username} 身份登录...")
        try:
            mail.login(username, password)
        except imaplib.IMAP4.error as e:
            print(f"IMAP错误: {str(e)}")
            # 尝试其他登录方式
            try:
                print("尝试使用明确的认证方式...")
                mail = imaplib.IMAP4_SSL(imap_server, imap_port)
                mail._simple_command('LOGIN', username, f'"{password}"')
                result, data = mail._untagged_response(b'OK', b'[CAPABILITY')
                print(f"结果: {result}")
            except Exception as e2:
                print(f"第二次尝试失败: {str(e2)}")
        
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

def main():
    """主函数"""
    print("===== Outlook IMAP邮件获取程序 =====\n")
    
    # 决定如何获取凭据
    if len(sys.argv) >= 3:
        username = sys.argv[1]
        password = sys.argv[2]
    else:
        # 交互式输入
        username = input("请输入您的Outlook邮箱地址: ")
        password = getpass.getpass("请输入您的邮箱密码(输入时不会显示): ")
    
    # 可选参数：是否标记为已读
    mark_as_read = False
    if len(sys.argv) >= 4 and sys.argv[3].lower() in ('true', 't', 'yes', 'y', '1'):
        mark_as_read = True
    
    # 获取邮件
    email_data = get_first_email_imap(username, password, mark_as_read)
    
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