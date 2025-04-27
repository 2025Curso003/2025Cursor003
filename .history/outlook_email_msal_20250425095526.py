import requests
import msal
import sys
import json

def get_first_email(client_id, refresh_token, username, password):
    """
    使用Microsoft Graph API获取Outlook邮箱中的第一封邮件
    
    参数:
        client_id (str): 应用程序的client_id
        refresh_token (str): 用户的刷新令牌
        username (str): Outlook邮箱账号
        password (str): Outlook邮箱密码
        
    返回:
        dict: 包含邮件详细信息的字典，如果失败则返回None
    """
    # 创建MSAL应用实例
    app = msal.PublicClientApplication(client_id)
    
    # 尝试使用刷新令牌获取新的访问令牌
    result = None
    
    # 首先尝试使用刷新令牌
    accounts = app.get_accounts()
    if accounts:
        # 如果已经有账户缓存，直接使用
        result = app.acquire_token_silent(["Mail.Read"], account=accounts[0])
    
    # 如果无法使用刷新令牌，尝试使用用户名和密码
    if not result:
        try:
            # 使用用户凭据获取令牌
            result = app.acquire_token_by_username_password(
                username, 
                password, 
                scopes=["Mail.Read"]
            )
        except Exception as e:
            print(f"使用用户名和密码获取令牌失败: {str(e)}")
            
            # 尝试使用刷新令牌（手动方式）
            try:
                token_url = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
                token_data = {
                    "client_id": client_id,
                    "grant_type": "refresh_token",
                    "refresh_token": refresh_token,
                    "scope": "Mail.Read"
                }
                token_response = requests.post(token_url, data=token_data)
                token_response.raise_for_status()
                result = token_response.json()
                print("使用刷新令牌成功获取访问令牌")
            except Exception as refresh_error:
                print(f"使用刷新令牌获取访问令牌失败: {str(refresh_error)}")
                return None
    
    # 检查是否成功获取令牌
    if "access_token" not in result:
        print(f"获取访问令牌失败: {result.get('error_description', '未知错误')}")
        return None
    
    access_token = result["access_token"]
    
    # 使用访问令牌获取邮件
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
    if len(sys.argv) != 5:
        print("使用方法: python outlook_email_msal.py <client_id> <refresh_token> <username> <password>")
        print("或者直接编辑脚本中的凭据信息")
        
        # 如果没有提供命令行参数，使用脚本中的默认值
        # 请将以下变量替换为您的实际信息
        client_id = "9e5f94bc-e8a4-4e73-b8be-63364c29d753"  # 替换为您的client_id
        refresh_token = "M.C538_BL2.0.U.-Cii8bsrQSt0FU5ajkl*JH6sVtO5I1iiOt*y7u*MgXRMv1TE94!hCiz*e3JjlcngGx4YNmEgbztt4WSXAGwFC51Kw9klYPUJPwt2fUqJb*aBg16ZZVeRrvTPTJ8rLfV3TmHoAwWIKX!rch5H06BprSuSpUxU1ct*!OnakHs3lI4FxOago4tqArHB2yTD5LcwnTGavrUlumkx!qQuukxLBomCtSXXmHy*p8gzvoaNDUOjXhsvtqhIq5XhbpF1gCDvcoXp*BlUEC9SZIcuq3gLmsFICJbnLSLy7!x3Jdq9wX4lIPRxJYv!vqVe1AxNrF8tdSc0c6BOmN3juHcBGRLcZJb6OVvpswcAbge6Ny!pIASiZxpwbC2VZCY1UyqoHahhuzmfo8DqQbJgkr43!mbuU8wpdNUQ7Aa69ooOtxCNxXgNgKRRuijqRslcGmTv!rqzrrhb5TOa7FVGJcB7ZWe1yXLc$"  # 替换为您的刷新令牌
        username = "jamescastanedasoa9413@outlook.com"  # 替换为您的Outlook邮箱
        password = "x"  # 替换为您的密码
    else:
        client_id = sys.argv[1]
        refresh_token = sys.argv[2]
        username = sys.argv[3]
        password = sys.argv[4]
    
    # 获取第一封邮件
    email = get_first_email(client_id, refresh_token, username, password)
    
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