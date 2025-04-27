# Outlook邮件获取器

这个项目提供了三种不同的方法来获取Outlook邮箱中的第一封邮件，使用Microsoft的OAuth 2.0认证和Microsoft Graph API。

## 文件说明

1. `outlook_first_email.py` - 基本版本，使用自定义OAuth流程
2. `outlook_email_msal.py` - 使用Microsoft Authentication Library (MSAL)的版本
3. `outlook_email_simple.py` - 最简单的版本，只使用刷新令牌

## 安装依赖

```bash
# 安装基本版本依赖
pip install requests

# 如果使用MSAL版本，还需安装
pip install msal
```

## 获取必要的凭据

要使用这些脚本，您需要：

1. **Client ID** - 从Microsoft Azure Portal注册应用后获取
2. **刷新令牌** - 可以通过OAuth流程获取
3. **邮箱账号和密码** - 您的Outlook账号凭据

### 如何获取Client ID

1. 访问 [Azure Portal](https://portal.azure.com/)
2. 创建新的应用注册
3. 配置重定向URI (例如 http://localhost)
4. 记下应用程序ID (Client ID)

### 如何获取刷新令牌

1. 使用授权码流程获取初始刷新令牌
2. 保存应用返回的刷新令牌

## 使用方法

### 简单版本 (只需要Client ID和刷新令牌)

```bash
python outlook_email_simple.py <client_id> <refresh_token>
```

### 完整版本 (需要Client ID、刷新令牌、邮箱账号和密码)

```bash
python outlook_first_email.py <client_id> <refresh_token> <username> <password>
```

### MSAL版本

```bash
python outlook_email_msal.py <client_id> <refresh_token> <username> <password>
```

## 注意事项

- 刷新令牌通常有较长的有效期，但最终也会过期
- 每次使用刷新令牌获取新的访问令牌时，也会返回新的刷新令牌
- 请妥善保管您的凭据信息，不要将其暴露在公共仓库中

# Cursor Pro 自动化工具使用说明


[English doc](./README.EN.md)

## 交流群 QQ 1034718338


## 在线文档
[cursor-auto-free-doc.vercel.app](https://cursor-auto-free-doc.vercel.app)


## 许可证声明
本项目采用 [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) 许可证。
这意味着您可以：
- 分享 — 在任何媒介以任何形式复制、发行本作品
但必须遵守以下条件：
- 非商业性使用 — 您不得将本作品用于商业目的

## 声明
- 本项目仅供学习交流使用，请勿用于商业用途。
- 本项目不承担任何法律责任，使用本项目造成的任何后果，由使用者自行承担。



## 骗子
海豚


## 感谢 linuxDo 这个开源社区(一个真正的技术社区)
https://linux.do/

## 特别鸣谢
本项目的开发过程中得到了众多开源项目和社区成员的支持与帮助，在此特别感谢：

### 开源项目
- [go-cursor-help](https://github.com/yuaotian/go-cursor-help) - 一个优秀的 Cursor 机器码重置工具，本项目的机器码重置功能使用该项目实现。该项目目前已获得 9.1k Stars，是最受欢迎的 Cursor 辅助工具之一。

## 请我喝杯茶
<img src="./screen/28613e3f3f23a935b66a7ba31ff4e3f.jpg" width="300"/> <img src="./screen/mm_facetoface_collect_qrcode_1738583247120.png" width="300"/>

## 关注公众号，随时获取仓库更新动态

![image](./screen/qrcode_for_gh_c985615b5f2b_258.jpg)


