# Outlook OAuth2 授权工具使用指南

该工具可以帮助您获取Microsoft Graph API需要的刷新令牌，用于访问Outlook邮箱内容。

## 使用步骤

### 1. 在Microsoft Azure Portal注册应用

1. 登录 [Azure Portal](https://portal.azure.com/)
2. 转到 **Azure Active Directory** -> **应用注册**
3. 点击 **新注册**
4. 填写以下信息:
   - **名称**: 任意名称，如 "Outlook Email Reader"
   - **支持的账户类型**: 选择 "任何组织目录中的账户和个人Microsoft账户"
   - **重定向URI**: 选择 "Web" 并输入 `http://localhost:8000`

5. 点击 **注册**
6. 在注册后的应用页面，记下 **应用程序(客户端) ID**

### 2. 配置API权限

1. 在您的应用页面，点击 **API权限**
2. 点击 **添加权限**
3. 选择 **Microsoft Graph**
4. 选择 **委托的权限**
5. 找到并选择以下权限:
   - `Mail.Read` (读取邮件)
   - `offline_access` (离线访问)
6. 点击 **添加权限**

### 3. 配置授权工具

1. 打开 `get_outlook_auth.py` 文件
2. 将您在第1步获取的**应用程序(客户端) ID**填入 `CLIENT_ID` 变量中:

```python
CLIENT_ID = "您的应用程序ID"  # 例如: "a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6"
```

### 4. 运行授权工具

1. 确保已安装必要的库:
```
pip install requests
```

2. 运行授权工具:
```
python get_outlook_auth.py
```

3. 工具会自动在浏览器中打开Microsoft登录页面
4. 使用您的Outlook账号登录
5. 授权应用访问您的邮件
6. 登录成功后，会显示"授权成功"页面，并自动生成 `outlook_tokens.json` 文件

### 5. 使用获取的刷新令牌

1. 打开生成的 `outlook_tokens.json` 文件
2. 找到 `refresh_token` 字段，复制其值
3. 在您的邮件读取脚本中更新刷新令牌值

例如:
```python
client_id = "您的应用程序ID"  # 与授权工具中使用的相同
refresh_token = "您刚获取的刷新令牌"
```

## 故障排除

### 授权失败

1. 确保您的应用注册中的重定向URI正确配置为 `http://localhost:8000`
2. 验证您已经为应用添加了正确的API权限
3. 尝试清除浏览器缓存和cookies后重试

### 令牌获取失败

1. 确保 `CLIENT_ID` 变量中填写的是正确的应用程序ID
2. 检查网络连接是否正常
3. 检查是否使用了正确的账号登录

## 注意事项

1. 刷新令牌通常有较长的有效期(几天到几十天)，但最终也会过期，届时需要再次运行此工具获取新令牌
2. 请妥善保管您的刷新令牌，不要将其分享给他人
3. 如果您的应用注册发生变更，可能需要重新获取授权 