import requests
import sys
import json

def debug_log(message):
    """打印调试信息"""
    print(f"[DEBUG] {message}")

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
        "scope": "Mail.Read offline_access"
    }
    
    debug_log(f"请求URL: {token_url}")
    debug_log(f"请求头: {headers}")
    debug_log(f"请求数据: {data}")
    
    try:
        response = requests.post(token_url, headers=headers, data=data)
        
        debug_log(f"响应状态码: {response.status_code}")
        debug_log(f"响应内容: {response.text}")
        
        if response.status_code == 200:
            token_data = response.json()
            debug_log("成功获取访问令牌")
            
            # 保存新的刷新令牌以备后用
            if "refresh_token" in token_data:
                debug_log(f"新的刷新令牌: {token_data['refresh_token']}")
                
                # 保存令牌到文件
                with open("outlook_latest_tokens.json", "w") as f:
                    json.dump(token_data, f, indent=4)
                debug_log("已将最新令牌保存到 outlook_latest_tokens.json 文件")
            
            return token_data["access_token"]
        else:
            debug_log(f"获取访问令牌失败: {response.status_code} - {response.text}")
            
            # 分析错误消息
            try:
                error_data = response.json()
                debug_log(f"错误类型: {error_data.get('error', '未知')}")
                debug_log(f"错误描述: {error_data.get('error_description', '未知')}")
                
                if "invalid_grant" in error_data.get('error', ''):
                    print("\n[提示] 刷新令牌可能已过期，请使用 get_outlook_auth.py 获取新的令牌")
            except:
                debug_log("无法解析错误响应为JSON")
            
            return None
    except Exception as e:
        debug_log(f"请求异常: {str(e)}")
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
    
    debug_log("准备获取邮件列表")
    
    try:
        # 获取收件箱中的第一封邮件
        messages_url = f"{graph_endpoint}/me/messages?$top=1"
        debug_log(f"请求URL: {messages_url}")
        debug_log(f"请求头: {headers}")
        
        messages_response = requests.get(messages_url, headers=headers)
        debug_log(f"响应状态码: {messages_response.status_code}")
        
        if messages_response.status_code != 200:
            debug_log(f"获取邮件列表失败: {messages_response.text}")
            return None
        
        messages_data = messages_response.json()
        debug_log(f"邮件列表响应: {json.dumps(messages_data, indent=2)[:500]}...")
        
        # 检查是否有邮件
        if not messages_data.get("value"):
            debug_log("邮箱中没有邮件")
            return None
        
        first_email = messages_data["value"][0]
        email_id = first_email["id"]
        debug_log(f"找到第一封邮件，ID: {email_id}")
        
        # 获取完整邮件内容
        email_url = f"{graph_endpoint}/me/messages/{email_id}"
        debug_log(f"请求邮件详情URL: {email_url}")
        
        email_response = requests.get(email_url, headers=headers)
        debug_log(f"响应状态码: {email_response.status_code}")
        
        if email_response.status_code != 200:
            debug_log(f"获取邮件详情失败: {email_response.text}")
            return None
        
        email_data = email_response.json()
        debug_log("成功获取邮件详情")
        
        # 提取并返回邮件信息
        result = {
            "id": email_data.get("id"),
            "subject": email_data.get("subject", "无主题"),
            "from": email_data.get("from", {}).get("emailAddress", {}).get("address", "未知发件人"),
            "received_date": email_data.get("receivedDateTime", "未知时间"),
            "body_preview": email_data.get("bodyPreview", ""),
            "body": email_data.get("body", {}).get("content", ""),
            "is_read": email_data.get("isRead", False)
        }
        
        debug_log(f"提取的邮件信息: {json.dumps(result, indent=2, ensure_ascii=False)[:500]}...")
        return result
    except Exception as e:
        debug_log(f"获取邮件过程中发生异常: {str(e)}")
        import traceback
        debug_log(f"异常堆栈: {traceback.format_exc()}")
        return None

def main():
    """主函数"""
    debug_log("开始执行Outlook邮件获取程序")
    
    # 确定参数来源
    if len(sys.argv) < 3:
        debug_log("未提供命令行参数，尝试从文件加载")
        
        # 尝试从令牌文件加载
        try:
            with open("outlook_tokens.json", "r") as f:
                tokens = json.load(f)
                client_id = tokens.get("client_id")
                refresh_token = tokens.get("refresh_token")
                
                if not client_id:
                    debug_log("令牌文件中没有client_id，尝试从配置获取")
                    # 如果文件中没有client_id，使用配置中的值
                    client_id = "YOUR_CLIENT_ID"  # 替换为您的client_id
                
                debug_log(f"从文件加载的client_id: {client_id}")
                debug_log(f"从文件加载的refresh_token: {refresh_token[:20]}...")
        except Exception as e:
            debug_log(f"从文件加载令牌失败: {str(e)}")
            
            # 使用配置值
            client_id = "YOUR_CLIENT_ID"  # 替换为您的client_id
            refresh_token = "YOUR_REFRESH_TOKEN"  # 替换为您的刷新令牌
            
            debug_log(f"使用配置中的client_id: {client_id}")
            debug_log(f"使用配置中的refresh_token: {refresh_token[:20] if len(refresh_token) > 20 else refresh_token}...")
    else:
        debug_log("使用命令行参数")
        client_id = sys.argv[1]
        refresh_token = sys.argv[2]
        
        debug_log(f"从命令行获取的client_id: {client_id}")
        debug_log(f"从命令行获取的refresh_token: {refresh_token[:20]}...")
    
    # 验证参数
    if client_id == "YOUR_CLIENT_ID" or refresh_token == "YOUR_REFRESH_TOKEN":
        print("错误: 请提供有效的client_id和refresh_token")
        print("您可以运行 get_outlook_auth.py 获取新的令牌")
        return
    
    # 获取访问令牌
    debug_log("开始获取访问令牌")
    access_token = get_access_token(client_id, refresh_token)
    
    if not access_token:
        print("无法获取访问令牌，请检查您的client_id和refresh_token")
        return
    
    # 获取第一封邮件
    debug_log("开始获取第一封邮件")
    email = get_first_email(access_token)
    
    if email:
        print("\n===== 邮件详情 =====")
        print(f"ID: {email['id']}")
        print(f"主题: {email['subject']}")
        print(f"发件人: {email['from']}")
        print(f"接收时间: {email['received_date']}")
        print(f"是否已读: {'是' if email['is_read'] else '否'}")
        print("\n----- 邮件内容预览 -----")
        print(email['body_preview'])
        print("\n----- 完整邮件内容 -----")
        print(email['body'])
        
        debug_log("程序成功完成")
    else:
        print("无法获取邮件")
        debug_log("程序完成，但未能获取邮件")

if __name__ == "__main__":
    print("===== Outlook邮件获取程序(调试版) =====\n")
    main() 