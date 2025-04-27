import logging
import time
import re
from config import Config
import requests
import email
import imaplib


class GetVerificationCodeGmail:
    def __init__(self):
        self.login_url_outlook = "https://mail.google.com/";

    def get_verification_code_outlook(self, browser, tab, account, password, max_retries=2, retry_interval=10):
        """
        获取验证码，带有重试机制。

        Args:
            max_retries: 最大重试次数。
            retry_interval: 重试间隔时间（秒）。

        Returns:
            验证码 (字符串或 None)。
        """

        for attempt in range(max_retries):
            try:
                logging.info(f"尝试获取验证码 (第 {attempt + 1}/{max_retries} 次)...")
    
                verify_code = self._get_mail_code_by_imap(browser, tab, account, password)
                if verify_code is not None:
                    return verify_code

                if attempt < max_retries - 1:  # 除了最后一次尝试，都等待
                    return 404

            except Exception as e:
                logging.error(f"获取验证码失败: {e}")  # 记录更一般的异常
                if attempt < max_retries - 1:
                    logging.error(f"发生错误，{retry_interval} 秒后重试...")
                    time.sleep(retry_interval)
                else:
                    raise Exception(f"获取验证码失败且已达最大重试次数: {e}") from e

        raise Exception(f"经过 {max_retries} 次尝试后仍未获取到验证码。")

    # 使用imap获取邮件
    def _get_mail_code_by_imap(self, browser, tab, account, password, retry=2):
        if retry > 0:
            time.sleep(3)
        if retry >= 3:
            raise Exception("获取验证码超时")
        try:
            # 打开浏览器新标签
            # 在打开新页面前清除所有数据
            # 在打开新页面前清除所有数据
             browser.run_cdp('Network.clearBrowserCache')  # 清除缓存
             browser.run_cdp('Network.clearBrowserCookies')  # 清除 cookies
            
            # 使用隐私模式打开新标签页
             logging.info(f"正在访问邮箱登录页面: {self.login_url_outlook}")
             # 打开新标签进行请求
             tab.get(self.login_url_outlook)
             time.sleep(2)  # 等待页面加载

             try:
                logging.info("正在填写邮箱...")
                email_input = tab.ele("@type=email")
                if email_input:
                    email_input.click().input(account)
                else:
                    logging.error("未找到邮箱输入框")
             except Exception as e:
                logging.error(f"未找到邮箱输入框: {e}")

             logging.info("提交邮箱信息...")
             next_button = tab.ele("span:contains('next')")
             if next_button:
                 logging.info("找到 'next' 按钮，正在点击...")
                 next_button.click()
             else:
                 logging.error("未找到 'next' 按钮")

             time.sleep(4)      
             try:
                logging.info("正在填写密码...")
                email_input = tab.ele("@type=password")
                if email_input:
                    email_input.click().input(password)
                else:
                    logging.error("未找到密码输入框")
                    
                logging.info(f"已输入密码......")
             except Exception as e:
                logging.error(f"未找到密码输入框: {e}")
             
             logging.info("提交密码信息...")
             tab.actions.click("@type=submit")
             time.sleep(2)
             logging.info("开始跳过保护...")
             max_attempts = 5 
             found = True # 最大尝试次数

             skip_elements = [
                    ("@id=declineButton", "点击no跳过declineButton"),
                    ("@data-testid=secondaryButton", "点击secondaryButton否跳过"),
                    ("@id=iShowSkip", "跳过skip001/002"),
                    ("@data-testid=secondaryButton", "否"),
                    ("@aria-label=暂时跳过", "点击aria-label=暂时跳过"),
                    ("@aria-label=No", "点击aria-label=No"),
                    ("@aria-label=Skip for now", "跳过skip003"),
                    ("@id=id__0", "点击id__0ok跳过"),
                    ("@id=id__8", "点击id__8ok跳过"),
                    
                    
                ]
             
             while max_attempts > 0:
                try:
                    # 检查所有可能的跳过按钮
                  
                    
                    if False == found:
                        break
                    
                    # 定义一个变量长度为skip_elements长度
                    skip_elements_length = len(skip_elements)
                    for selector, log_msg in skip_elements:
                        logging.info(f"开始查找selector: {selector}")
                        
                        element = tab.ele(selector)
                        if element:
                            logging.info(log_msg)
                            # 变量长度减1
                            skip_elements_length -= 1
                            element.click()
                            time.sleep(2)
                            if log_msg == "点击no跳过declineButton":
                                found = False
                                break
                            if log_msg == "点击id__8ok跳过":
                                found = False
                                break
                            if log_msg == "点击secondaryButton否跳过":
                                found = False
                                break
                            if log_msg == "否":
                                found = False
                                break
                            found = True
                            break
                    if not found:
                        logging.info("没有找到需要跳过的元素，退出循环")
                        break
                    if skip_elements_length == len(skip_elements):
                        logging.info("没有找到需要跳过的元素，退出循环")
                        break;
                except Exception as e:
                    logging.error(f"处理跳过按钮时出错: {e}")
                
                max_attempts -= 1

             
             logging.info("保护跳过完成...")
             time.sleep(10)
             logging.info("睡眠8秒完成...")
             # 循环获取三次
             for i in range(6):
                html_content = tab.html
                #在html中寻找字符 Your one-time code is,如果存在则提取验证码
                code_match = re.search(r"Your verification code is (\d{6})", html_content)
                if code_match:
                 logging.info(f"得到验证码: {code_match.group(1)}")
                 return code_match.group(1)  # 返回匹配的6位数字
                else:
                    logging.info("没有找到验证码，睡眠2秒继续获取...")
                    # 睡眠5秒
                    time.sleep(4)
                
        except Exception as e:
            print(f"发生错误: {e}")
            return None
        
    def _extract_imap_body(self, email_message):
        # 提取邮件正文
        if email_message.is_multipart():
            for part in email_message.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))
                if content_type == "text/plain" and "attachment" not in content_disposition:
                    charset = part.get_content_charset() or 'utf-8'
                    try:
                        body = part.get_payload(decode=True).decode(charset, errors='ignore')
                        return body
                    except Exception as e:
                        logging.error(f"解码邮件正文失败: {e}")
        else:
            content_type = email_message.get_content_type()
            if content_type == "text/plain":
                charset = email_message.get_content_charset() or 'utf-8'
                try:
                    body = email_message.get_payload(decode=True).decode(charset, errors='ignore')
                    return body
                except Exception as e:
                    logging.error(f"解码邮件正文失败: {e}")
        return ""

    # 手动输入验证码
    def _get_latest_mail_code(self):
        # 获取邮件列表
        mail_list_url = f"https://tempmail.plus/api/mails?email={self.username}{self.emailExtension}&limit=20&epin={self.epin}"
        mail_list_response = self.session.get(mail_list_url)
        mail_list_data = mail_list_response.json()
        time.sleep(0.5)
        if not mail_list_data.get("result"):
            return None, None

        # 获取最新邮件的ID
        first_id = mail_list_data.get("first_id")
        if not first_id:
            return None, None

        # 获取具体邮件内容
        mail_detail_url = f"https://tempmail.plus/api/mails/{first_id}?email={self.username}{self.emailExtension}&epin={self.epin}"
        mail_detail_response = self.session.get(mail_detail_url)
        mail_detail_data = mail_detail_response.json()
        time.sleep(0.5)
        if not mail_detail_data.get("result"):
            return None, None

        # 从邮件文本中提取6位数字验证码
        mail_text = mail_detail_data.get("text", "")
        mail_subject = mail_detail_data.get("subject", "")
        logging.info(f"找到邮件主题: {mail_subject}")
        # 修改正则表达式，确保 6 位数字不紧跟在字母或域名相关符号后面
        code_match = re.search(r"(?<![a-zA-Z@.])\b\d{6}\b", mail_text)

        if code_match:
            return code_match.group(), first_id
        return None, None

    def _cleanup_mail(self, first_id):
        # 构造删除请求的URL和数据
        delete_url = "https://tempmail.plus/api/mails/"
        payload = {
            "email": f"{self.username}{self.emailExtension}",
            "first_id": first_id,
            "epin": f"{self.epin}",
        }

        # 最多尝试5次
        for _ in range(5):
            response = self.session.delete(delete_url, data=payload)
            try:
                result = response.json().get("result")
                if result is True:
                    return True
            except:
                pass

            # 如果失败,等待0.5秒后重试
            time.sleep(0.5)

        return False


if __name__ == "__main__":
    email_handler = GetVerificationCodeOutLook()
    
    # 初始化浏览器
    from browser_utils_email import BrowserManagerEmail
    browser_manager = BrowserManagerEmail()
    browser = browser_manager.init_browser()
    tab = browser.latest_tab
    
    try:
        code = email_handler.get_verification_code(browser, tab)
        print(code)
    finally:
        browser_manager.quit()  # 确保浏览器被关闭