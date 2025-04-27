import requests
import sys
import json

def get_access_token(client_id, refresh_token):
    """
    使用刷新令牌获取访问令牌
    
    参数:
        client_id (str): 应用程序的client_id
        refresh_token (str): 用户的刷新令牌
        
    返回:
        str: 访问令牌，如果失败则返回None
    """
    token_url = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    data = {
        "client_id": client_id,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
        "scope": "Mail.Read"
    }
    
    try:
        response = requests.post(token_url, headers=headers, data=data)
        response.raise_for_status()
        token_data = response.json()
        
        if "access_token" not in token_data:
            print(f"获取访问令牌失败: {token_data.get('error_description', '未知错误')}")
            return None
            
        print("成功获取访问令牌")
        # 保存新的刷新令牌以备后用
        if "refresh_token" in token_data:
            print(f"新的刷新令牌: {token_data['refresh_token']}")
            
        return token_data["access_token"]
    except Exception as e:
        print(f"获取访问令牌失败: {str(e)}")
        return None

def get_first_email(access_token):
    """
    使用访问令牌获取第一封邮件
    
    参数:
        access_token (str): Microsoft Graph API的访问令牌
        
    返回:
        dict: 包含邮件详细信息的字典，如果失败则返回None
    """
    graph_endpoint = "https://graph.microsoft.com/v1.0"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    try:
        # 获取收件箱中的第一封邮件
        messages_url = f"{graph_endpoint}/me/messages?$top=1"
        messages_response = requests.get(messages_url, headers=headers)
        messages_response.raise_for_status()
        messages_data = messages_response.json()
        
        # 检查是否有邮件
        if not messages_data.get("value"):
            print("邮箱中没有邮件")
            return None
        
        first_email = messages_data["value"][0]
        email_id = first_email["id"]
        
        # 获取完整邮件内容
        email_url = f"{graph_endpoint}/me/messages/{email_id}"
        email_response = requests.get(email_url, headers=headers)
        email_response.raise_for_status()
        email_data = email_response.json()
        
        # 提取并返回邮件信息
        return {
            "id": email_data.get("id"),
            "subject": email_data.get("subject", "无主题"),
            "from": email_data.get("from", {}).get("emailAddress", {}).get("address", "未知发件人"),
            "received_date": email_data.get("receivedDateTime", "未知时间"),
            "body_preview": email_data.get("bodyPreview", ""),
            "body": email_data.get("body", {}).get("content", ""),
            "is_read": email_data.get("isRead", False)
        }
    except Exception as e:
        print(f"获取邮件失败: {str(e)}")
        return None

def main():
    """主函数"""
    if len(sys.argv) < 3:
        print("使用方法: python outlook_email_simple.py <client_id> <refresh_token>")
        print("或者直接编辑脚本中的凭据信息")
        
        # 如果没有提供命令行参数，使用脚本中的默认值
        # 请将以下变量替换为您的实际信息
        client_id = "YOUR_CLIENT_ID"  # 替换为您的client_id
        refresh_token = "YOUR_REFRESH_TOKEN"  # 替换为您的刷新令牌
    else:
        client_id = sys.argv[1]
        refresh_token = sys.argv[2]
    
    # 验证所有必需的参数
    if client_id == "YOUR_CLIENT_ID" or refresh_token == "YOUR_REFRESH_TOKEN":
        print("错误: 请提供有效的client_id和refresh_token")
        sys.exit(1)
    
    # 获取访问令牌
    access_token = get_access_token(client_id, refresh_token)
    if not access_token:
        print("无法获取访问令牌，请检查您的client_id和refresh_token")
        sys.exit(1)
    
    # 获取第一封邮件
    email = get_first_email(access_token)
    
    if email:
        print("\n==== 邮件详情 ====")
        print(f"ID: {email['id']}")
        print(f"主题: {email['subject']}")
        print(f"发件人: {email['from']}")
        print(f"接收时间: {email['received_date']}")
        print(f"是否已读: {'是' if email['is_read'] else '否'}")
        print("\n---- 邮件内容预览 ----")
        print(email['body_preview'])
        print("\n---- 完整邮件内容 ----")
        print(email['body'])
    else:
        print("无法获取邮件")

if __name__ == "__main__":
    main() 