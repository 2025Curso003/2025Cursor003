import requests
import base64
import json
import sys

class OutlookEmailFetcher:
    def __init__(self, client_id, refresh_token, username, password):
        """
        初始化OutlookEmailFetcher类
        
        参数:
            client_id (str): 应用的client_id
            refresh_token (str): 用户的刷新令牌
            username (str): Outlook邮箱账号
            password (str): Outlook邮箱密码
        """
        self.client_id = client_id
        self.refresh_token = refresh_token
        self.username = username
        self.password = password
        self.access_token = None
        self.token_endpoint = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
        self.graph_endpoint = "https://graph.microsoft.com/v1.0"
    
    def refresh_access_token(self):
        """
        使用刷新令牌获取新的访问令牌
        
        返回:
            bool: 是否成功刷新访问令牌
        """
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        data = {
            "client_id": self.client_id,
            "refresh_token": self.refresh_token,
            "grant_type": "refresh_token",
            "scope": "Mail.Read"
        }
        
        try:
            response = requests.post(self.token_endpoint, headers=headers, data=data)
            response.raise_for_status()
            token_data = response.json()
            self.access_token = token_data.get("access_token")
            
            # 如果成功获取到新的刷新令牌，更新它
            if "refresh_token" in token_data:
                self.refresh_token = token_data.get("refresh_token")
                print("刷新令牌已更新")
            
            return self.access_token is not None
        except Exception as e:
            print(f"刷新访问令牌失败: {str(e)}")
            return False
    
    def get_first_email(self):
        """
        获取邮箱中的第一封邮件
        
        返回:
            dict: 包含邮件内容的字典
        """
        # 首先刷新访问令牌
        if not self.refresh_access_token():
            print("无法获取访问令牌，退出操作")
            return None
        
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        # 获取收件箱中前1封邮件
        try:
            url = f"{self.graph_endpoint}/me/messages?$top=1"
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            emails = response.json().get("value", [])
            
            if not emails:
                print("邮箱中没有找到邮件")
                return None
            
            first_email = emails[0]
            
            # 获取邮件详细内容（如果需要）
            email_id = first_email.get("id")
            detail_url = f"{self.graph_endpoint}/me/messages/{email_id}"
            detail_response = requests.get(detail_url, headers=headers)
            detail_response.raise_for_status()
            email_detail = detail_response.json()
            
            return {
                "id": email_detail.get("id"),
                "subject": email_detail.get("subject", "无主题"),
                "from": email_detail.get("from", {}).get("emailAddress", {}).get("address", "未知发件人"),
                "received_date": email_detail.get("receivedDateTime", "未知时间"),
                "body_preview": email_detail.get("bodyPreview", ""),
                "body": email_detail.get("body", {}).get("content", ""),
                "is_read": email_detail.get("isRead", False)
            }
        except Exception as e:
            print(f"获取邮件失败: {str(e)}")
            return None

def main():
    """主函数"""
    if len(sys.argv) != 5:
        print("使用方法: python outlook_first_email.py <client_id> <refresh_token> <username> <password>")
        print("或者直接编辑脚本中的凭据信息")
        
        # 如果没有提供命令行参数，使用脚本中的默认值
        # 请将以下变量替换为您的实际信息
        client_id = "YOUR_CLIENT_ID"  # 替换为您的client_id
        refresh_token = "YOUR_REFRESH_TOKEN"  # 替换为您的刷新令牌
        username = "YOUR_OUTLOOK_EMAIL"  # 替换为您的Outlook邮箱
        password = "YOUR_PASSWORD"  # 替换为您的密码
    else:
        client_id = sys.argv[1]
        refresh_token = sys.argv[2]
        username = sys.argv[3]
        password = sys.argv[4]
    
    # 验证所有必需的参数
    if client_id == "YOUR_CLIENT_ID" or refresh_token == "YOUR_REFRESH_TOKEN" or username == "YOUR_OUTLOOK_EMAIL" or password == "YOUR_PASSWORD":
        print("错误: 请提供有效的client_id、refresh_token、username和password")
        sys.exit(1)
    
    # 创建邮件获取器实例
    fetcher = OutlookEmailFetcher(client_id, refresh_token, username, password)
    
    # 获取第一封邮件
    email = fetcher.get_first_email()
    
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