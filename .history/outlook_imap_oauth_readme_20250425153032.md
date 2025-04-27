# Outlook OAuth IMAP 邮件获取工具

这个Python脚本结合了OAuth 2.0身份验证和IMAP协议来访问Outlook邮箱，获取最新邮件。这种方法兼具OAuth的安全性和IMAP的高效性，是访问Microsoft邮件服务的推荐方式。

## 功能特点

- 使用OAuth 2.0进行安全认证，无需存储密码
- 通过IMAP协议高效地访问邮箱内容
- 支持访问令牌自动刷新机制
- 自动保存和加载令牌，避免重复授权
- 支持解析各种格式的邮件（纯文本、HTML）
- 可选择是否将邮件标记为已读
- 完整提取邮件头信息和正文内容

## 使用要求

1. Python 3.6 或更高版本
2. 必要的Python库：`requests`（可通过 `pip install requests` 安装）
3. Outlook.com 或 Office 365 邮箱账号
4. Microsoft Azure应用注册（已预配置，通常无需更改）

## 工作原理

此脚本使用以下流程访问您的邮件：

1. **OAuth 2.0授权**：使用Microsoft的授权流程获取访问令牌
2. **IMAP认证**：使用访问令牌通过XOAUTH2机制登录IMAP服务器
3. **邮件获取**：使用IMAP协议获取邮箱中的最新邮件
4. **令牌管理**：自动保存和刷新令牌，减少重复授权需求

## 使用方法

### 首次使用

首次运行脚本时，会触发OAuth授权流程：

```bash
python outlook_imap_oauth.py
```

脚本会：
1. 提示您输入Outlook邮箱地址
2. 在浏览器中打开Microsoft登录页面
3. 要求您登录并授权应用访问您的邮箱
4. 授权成功后自动获取访问令牌并保存
5. 使用令牌通过IMAP获取您的最新邮件

### 后续使用

后续运行脚本时，会尝试使用保存的令牌：

```bash
python outlook_imap_oauth.py
```

此时只需输入您的邮箱地址，无需重新授权（除非令牌已过期且无法刷新）。

## 配置选项

通常您不需要修改任何配置，但如果需要，可以在脚本中更改以下参数：

```python
# 客户端配置
client_id = "db3127ee-cc97-4566-bdd7-0b22bb5b7968"  # 应用ID
client_secret = ""  # 公共客户端应用通常不需要密钥
redirect_uri = "http://localhost:8000"  # 本地重定向URI
scopes = "offline_access https://outlook.office.com/IMAP.AccessAsUser.All"  # 权限范围
```

## 常见问题解答

### Q: 脚本请求过多的权限？

A: 脚本仅请求两个权限：
   - `offline_access`：允许获取刷新令牌
   - `IMAP.AccessAsUser.All`：允许通过IMAP访问您的邮件

### Q: 我的令牌安全吗？

A: 令牌保存在本地文件 `outlook_oauth_tokens.json` 中。请确保此文件不被他人访问。访问令牌通常有效期为1小时，刷新令牌可能持续数天或数周。

### Q: 授权后浏览器显示错误页面？

A: 确保本地端口8000未被其他应用占用。如果需要，可以修改脚本中的 `redirect_uri` 使用不同端口。

### Q: 为什么要结合OAuth和IMAP使用？

A: 
- OAuth提供更安全的身份验证，无需存储密码
- 支持多因素认证和条件访问策略
- 可细粒度控制访问权限
- IMAP提供高效的邮件访问机制

## 故障排除

### 授权失败

如果授权过程失败：
1. 确保您的网络连接正常
2. 检查浏览器是否阻止了弹出窗口
3. 尝试清除浏览器缓存和Cookie
4. 确保正确登录了对应的Microsoft账户

### IMAP连接失败

如果IMAP连接失败：
1. 确认您的Outlook账户支持IMAP访问
2. 检查网络连接和防火墙设置
3. 验证您输入的邮箱地址是否正确

### 令牌刷新失败

如果令牌刷新失败：
1. 删除 `outlook_oauth_tokens.json` 文件
2. 重新运行脚本，完成新的授权流程 