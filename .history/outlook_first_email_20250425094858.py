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
    
    def get_access_token(self):
        """
        使用刷新令牌获取新的访问令牌
        
        返回:
            str: 访问令牌
        """
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        # 尝试添加更多必需参数
        data = {
            "client_id": self.client_id,
            "refresh_token": self.refresh_token,
            "grant_type": "refresh_token",
            "scope": "Mail.Read offline_access", # 添加offline_access以获取新的刷新令牌
            "redirect_uri": "http://localhost" # 添加与应用注册时相同的重定向URI
        }
        
        try:
            # 打印请求信息以便调试
            print(f"请求URL: {self.token_endpoint}")
            print(f"请求头: {headers}")
            print(f"请求数据: {data}")
            
            response = requests.post(self.token_endpoint, headers=headers, data=data)
            
            # 打印响应信息
            print(f"响应状态码: {response.status_code}")
            print(f"响应内容: {response.text}")
            
            response.raise_for_status()
            token_data = response.json()
            
            if "access_token" not in token_data:
                print(f"获取访问令牌失败: {token_data.get('error_description', '未知错误')}")
                return None
            
            print("成功获取访问令牌")
            # 保存新的刷新令牌以备后用
            if "refresh_token" in token_data:
                print(f"新的刷新令牌: {token_data['refresh_token']}")
            
            self.access_token = token_data["access_token"]
            self.refresh_token = token_data.get("refresh_token")
            
            return self.access_token
        except Exception as e:
            print(f"获取访问令牌失败: {str(e)}")
            print(f"详细错误信息: {getattr(e, 'response', {}).get('text', '')}")
            return None
    
    def get_first_email(self):
        """
        获取邮箱中的第一封邮件
        
        返回:
            dict: 包含邮件内容的字典
        """
        # 首先刷新访问令牌
        if not self.get_access_token():
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
        client_id = "9e5f94bc-e8a4-4e73-b8be-63364c29d753"  # 替换为您的client_id
        refresh_token = "M.C557_BAY.0.U.-ClPTPu1BowsZ3N8YLlG6GqXw2mqLL!Xta61cPNjaHSuB7UgJpx8AwE5X4V3YDdb6t2NE0AjiqOSmCMUtRVRzHLZNbQGLHAUNiTWiXC!oK4A1za8aiXj6wrK9IfI9FWf6YuNe2ExEVPlx7p!3HggfIQ47tJgBwnlDlAJwWKHWue7tfVMGVpWNai3wz!5SvhV0LteuUaV*BdJyN*iSnW7G8AMMO97HO7DQHaTAArQITaqzpisulYPs!W1w!4UhWI0h0dJ5AAlLwFsoR5aKikQ2n1mgE4lBIXVi2rddqOczOzvjrkCA77dh30hZ59wuXvieu0EwZSfWJC9rvMZklVCq*BTHb8vkCvLHuyoEKDuT4P8KWmZOtjfC*jGH5s*JS*6JPYrq5KUmUFCFwCDSbvu2ReMR3uYMuUOxOmNwuNWI2b6t"  # 替换为您的刷新令牌
        username = "FrancoWilliam4481@outlook.com"  # 替换为您的Outlook邮箱
        password = "gmcm98022"  # 替换为您的密码
    else:
        client_id = sys.argv[1]
        refresh_token = sys.argv[2]
        username = sys.argv[3]
        password = sys.argv[4]
    
    
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