import os
import platform
import json
import sys
from colorama import Fore, Style
from enum import Enum
from typing import Optional
import secrets
import hashlib
import base64
import re
import uuid
import queue
import requests
import threading

from exit_cursor import ExitCursor
import go_cursor_help
import patch_cursor_get_machine_id
from reset_machine import MachineIDResetter
from get_email_code import EmailVerificationHandler
os.environ["PYTHONVERBOSE"] = "0"
os.environ["PYINSTALLER_VERBOSE"] = "0"

import time
import random
from cursor_auth_manager import CursorAuthManager
import os
os.environ['LANGUAGE'] = 'en_US.UTF-8'
from logger import logging
from browser_utils import BrowserManager
from get_verification_code_gmail import GetVerificationCodeGmail
from get_verification_code_outlook import GetVerificationCodeOutLook
from get_verification_code_163 import GetVerificationCode163
from logo import print_logo
from config import Config
from datetime import datetime, timedelta
import pymysql
from ConfigEmail import ConfigEmail
from fake_useragent import UserAgent

# 定义 EMOJI 字典
EMOJI = {"ERROR": "❌", "WARNING": "⚠️", "INFO": "ℹ️"}


class VerificationStatus(Enum):
    """验证状态枚举"""

    PASSWORD_PAGE = "@name=password"
    CAPTCHA_PAGE = "@data-index=0"
    ACCOUNT_SETTINGS = "Account Settings"


class TurnstileError(Exception):
    """Turnstile 验证相关异常"""

    pass


def save_screenshot(tab, stage: str, timestamp: bool = True) -> None:
    """
    保存页面截图

    Args:
        tab: 浏览器标签页对象
        stage: 截图阶段标识
        timestamp: 是否添加时间戳
    """
    try:
        # 创建 screenshots 目录
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        # 生成文件名
        if timestamp:
            filename = f"turnstile_{stage}_{int(time.time())}.png"
        else:
            filename = f"turnstile_{stage}.png"

        filepath = os.path.join(screenshot_dir, filename)

        # 保存截图
        tab.get_screenshot(filepath)
        logging.debug(f"截图已保存: {filepath}")
    except Exception as e:
        logging.warning(f"截图保存失败: {str(e)}")


def check_verification_success(tab) -> Optional[VerificationStatus]:
    """
    检查验证是否成功

    Returns:
        VerificationStatus: 验证成功时返回对应状态，失败返回 None
    """
    for status in VerificationStatus:
        if tab.ele(status.value):
            logging.info(f"验证成功 - 已到达{status.name}页面")
            return status
    return None


def handle_turnstile(tab, max_retries: int = 2, retry_interval: tuple = (1, 2)) -> bool:
    """
    处理 Turnstile 验证

    Args:
        tab: 浏览器标签页对象
        max_retries: 最大重试次数
        retry_interval: 重试间隔时间范围(最小值, 最大值)

    Returns:
        bool: 验证是否成功

    Raises:
        TurnstileError: 验证过程中出现异常
    """
    logging.info("正在检测 Turnstile 验证...")
    save_screenshot(tab, "start")

    retry_count = 0

    try:
        while retry_count < max_retries:
            retry_count += 1
            logging.debug(f"第 {retry_count} 次尝试验证")

            try:
                # 定位验证框元素
                challenge_check = (
                    tab.ele("@id=cf-turnstile", timeout=2)
                    .child()
                    .shadow_root.ele("tag:iframe")
                    .ele("tag:body")
                    .sr("tag:input")
                )

                if challenge_check:
                    logging.info("检测到 Turnstile 验证框，开始处理...")
                    # 随机延时后点击验证
                    time.sleep(random.uniform(1, 3))
                    challenge_check.click()
                    time.sleep(2)
                    logging.info("点击 Turnstile 验证...")
                    # 保存验证后的截图
                    save_screenshot(tab, "clicked")
                    # 检查验证结果
                    if check_verification_success(tab):
                        logging.info("Turnstile 验证通过")
                        save_screenshot(tab, "success")
                        return True

            except Exception as e:
                logging.debug(f"当前尝试未成功: {str(e)}")

            # 检查是否已经验证成功
            if check_verification_success(tab):
                return True

            # 随机延时后继续下一次尝试
            time.sleep(random.uniform(*retry_interval))

        # 超出最大重试次数
        logging.error(f"验证失败 - 已达到最大重试次数 {max_retries}")

        save_screenshot(tab, "failed")
        return False

    except Exception as e:
        error_msg = f"Turnstile 验证过程发生异常: {str(e)}"
        logging.error(error_msg)
        save_screenshot(tab, "error")
        raise TurnstileError(error_msg)


def get_cursor_session_token(tab, browser_manager=None, max_attempts: int = 3, retry_interval: int = 2) :
    """
    获取Cursor会话token
    
    Args:
        tab: 浏览器标签页对象
        browser: 浏览器实例对象
        max_attempts: 最大尝试次数
        retry_interval: 重试间隔(秒)
        
    Returns:
        Tuple[str, str] | None: 成功返回(userId, accessToken)元组，失败返回None
    """
    logging.info("开始获取会话令牌")
    
    # 首先尝试使用UUID深度登录方式
    logging.info("尝试使用深度登录方式获取token")
    
    def _generate_pkce_pair():
        """生成PKCE验证对"""
        code_verifier = secrets.token_urlsafe(43)
        code_challenge_digest = hashlib.sha256(code_verifier.encode('utf-8')).digest()
        code_challenge = base64.urlsafe_b64encode(code_challenge_digest).decode('utf-8').rstrip('=')    
        return code_verifier, code_challenge
    
    attempts = 0
    while attempts < max_attempts:
        try:
            verifier, challenge = _generate_pkce_pair()
            id = uuid.uuid4()
            client_login_url = f"https://www.cursor.com/cn/loginDeepControl?challenge={challenge}&uuid={id}&mode=login"
            
            logging.info(f"访问深度登录URL: {client_login_url}")
            tab.get(client_login_url)
            save_screenshot(tab, f"deeplogin_attempt_{attempts}")
            
            if tab.ele("xpath=//span[contains(text(), 'Yes, Log In')]", timeout=5):
                logging.info("点击确认登录按钮")
                tab.ele("xpath=//span[contains(text(), 'Yes, Log In')]").click()
                time.sleep(5)
                
                auth_poll_url = f"https://api2.cursor.sh/auth/poll?uuid={id}&verifier={verifier}"
                logging.info(f"得到原来的user-agent: {tab.run_js('return navigator.userAgent')}")
                headers = {
                    "User-Agent": tab.run_js('return navigator.userAgent'),
                    "Accept": "*/*"
                }
                
                logging.info(f"轮询认证状态: {auth_poll_url}")
                response = requests.get(auth_poll_url, headers=headers, timeout=15)
                
                if response.status_code == 200:
                    data = response.json()
                    accessToken = data.get("accessToken", None)
                    authId = data.get("authId", "")
                    
                    if accessToken:
                        userId = ""
                        if len(authId.split("|")) > 1:
                            userId = authId.split("|")[1]
                        
                        logging.info("成功获取账号token和userId")
                        return accessToken
                else:
                    logging.error(f"API请求失败，状态码: {response.status_code}")
            else:
                logging.warning("未找到登录确认按钮")
                # 尝试切换代理
                # logging.warning("------尝试切换代理------")
                # # 尝试为当前浏览器切换新代理
                # if browser_manager and browser_manager.switch_proxy():
                #     logging.info("成功切换到新代理")
                # else:
                #     logging.error("切换代理失败")
                
            attempts += 1
            if attempts < max_attempts:
                wait_time = retry_interval * attempts  # 逐步增加等待时间
                logging.warning(f"第 {attempts} 次尝试未获取到token，{wait_time}秒后重试...")
                save_screenshot(tab, f"token_attempt_{attempts}")
                time.sleep(wait_time)
                
        except Exception as e:
            logging.error(f"深度登录获取token失败: {str(e)}")
            attempts += 1
            save_screenshot(tab, f"token_error_{attempts}")
            if attempts < max_attempts:
                wait_time = retry_interval * attempts
                logging.warning(f"将在 {wait_time} 秒后重试...")
                time.sleep(wait_time)


def update_cursor_auth(email=None, access_token=None, refresh_token=None):
    """
    更新Cursor的认证信息的便捷函数
    """
    auth_manager = CursorAuthManager()
    return auth_manager.update_auth(email, access_token, refresh_token)


def sign_up_account(browser_manager, tab, email, email_password, client_id, refresh_token, get_email_type, proxy_ip=None):
    logging.info("=== 开始注册账号流程 ===")
    logging.info(f"正在访问注册页面: {sign_up_url}")
    tab.get(sign_up_url)

    max_retries = 1
    retry_count = 1

    while retry_count <= max_retries:
        try:
            if tab.ele("@name=first_name"):
                logging.info("正在填写个人信息...")
                tab.actions.click("@name=first_name").input(first_name)
                logging.info(f"已输入名字: {first_name}")
                time.sleep(random.uniform(1, 3))

                tab.actions.click("@name=last_name").input(last_name)
                logging.info(f"已输入姓氏: {last_name}")
                time.sleep(random.uniform(1, 3))

                tab.actions.click("@name=email").input(email)
                logging.info(f"已输入邮箱: {email}")
                time.sleep(random.uniform(1, 3))

                logging.info("提交个人信息...")
                tab.actions.click("@type=submit")
                
                time.sleep(random.uniform(2, 3))
                if tab.ele("Can't verify the user is human. Please try again."):
                    logging.error("无法验证是否是人类，重新设置代理...")
                    # 设置email use_status=0
                    update_email_use_status(email, 0)
                    return False
            else:
                logging.error("注册页面访问失败")
                update_email_use_status(email, 0)
                return False
        except Exception as e:
            logging.error(f"注册页面访问失败: {str(e)}")
            update_email_use_status(email, 0)
            return False

        if handle_turnstile(tab, max_retries=2, retry_interval=(1,2)):
            break
        else:
            # if tab.ele("Can't verify the user is human. Please try again."):
            logging.error("无法验证是否是人类，重新设置代理...")
            # 设置email use_status=0
            update_email_use_status(email, 0)
            return False
        retry_count += 1
            

    try:
        if tab.ele("@name=password"):
            logging.info("正在设置密码...")
            tab.ele("@name=password").input(password)
            time.sleep(random.uniform(1, 3))

            logging.info("提交密码...")
            tab.ele("@type=submit").click()
            logging.info("密码设置完成，等待系统响应...")
            time.sleep(random.uniform(2, 3))
            handle_turnstile(tab,max_retries=1,retry_interval=(1,2))
            if tab.ele("Can't verify the user is human. Please try again."):
                logging.error("无法验证是否是人类，重新设置代理...")
                # 设置email use_status=0
                update_email_use_status(email, 0)
                return False
    except Exception as e:
        logging.error(f"密码设置失败: {str(e)}")
        update_email_use_status(email, 0)
        return False

    if tab.ele("This email is not available."):
        logging.error("注册失败：邮箱已被使用")
        return False

    

    from browser_utils_email import BrowserManagerEmail
    browser_email_manager = None
    retry_count = 0  # 初始化重试计数器
    while True:
        try:
            # if tab.ele("Account Settings"):
            #     logging.info("注册成功 - 已进入账户设置页面")
            #     break
            if tab.ele("@data-index=0"):
                logging.info("正在获取邮箱验证码...")

            # 初始化浏览器
            # browser_email_manager = BrowserManagerEmail()
            handle_turnstile(tab,max_retries=1,retry_interval=(1,2))
            # 获取邮箱验证码    
            if get_email_type == 1:
                from outlook_imap_oauth_direct import get_verification_code
                try:
                    logging.info("通过 IMAP OAuth 获取 Outlook 验证码...")
                    # 随机睡眠5到8秒
                    time.sleep(random.uniform(1, 3))
                    code = get_verification_code(email, client_id, refresh_token, proxy_ip)
                    # 得到当前页面的 url
                    current_url = tab.run_js("return window.location.href")
                    logging.info(f"当前页面URL: {current_url}")
                    if code:
                        logging.info(f"成功获取验证码: {code}")
                    else:
                        logging.error("未能获取到有效的验证码")
                except Exception as e:
                    logging.error(f"获取验证码失败: {str(e)}")
                    code = None
            
            if get_email_type == 2:
                # # 初始化浏览器
                browser_email_manager = BrowserManagerEmail()
                
            # if email.endswith("@7to.us") or email.endswith("@gmail.com"):
               
            #     # 获取邮箱验证码
            #     email_handler = GetVerificationCodeGmail() 
            #     browserEmail = browser_email_manager.init_browser()
            #     tabEmail = browserEmail.latest_tab
            #     code = email_handler.get_verification_code_gmail(browserEmail, tabEmail, email, email_password)
      
                
            # if email.endswith("@outlook.com") or email.endswith("@hotmail.com"):
               
            #     # 获取邮箱验证码
                email_handler = GetVerificationCodeOutLook() 
                browserEmail = browser_email_manager.init_browser()
                tabEmail = browserEmail.latest_tab
                code = email_handler.get_verification_code_outlook(browserEmail, tabEmail, email, email_password)
            

            # if email.endswith("@163.com") :
            #         # 获取邮箱验证码
            #     email_handler = GetVerificationCode163()
            #     browserEmail = browser_email_manager.init_browser()
            #     tabEmail = browserEmail.latest_tab 
            #     code = email_handler.get_verification_code_163(browserEmail, tabEmail, email, email_password)    
            # try:
            #     logging.info("正在获取 apiget.com 邮箱验证码...")
            #     # 设置最大等待时间为10秒
            #     response = requests.get(
            #         f"https://00mail.cn/prod-api/email/api/stand/getNewEmailContent?email={email}",
            #         timeout=20
            #     )
            #     email_content = response.text
            #     logging.info(f"邮件内容: {email_content}")
            #     # 使用正则表达式查找验证码
            #     code_match = re.search(r"\b\d{6}\b", email_content)
            #     logging.info(f"验证码: {code_match}")
            #     if code_match:
            #         # 提取数字并移除空格
            #         logging.info(f"成功获取 apiget.com 验证码: {code_match.group()}")
            #         code = code_match.group()
            #     else:
            #         logging.error("未能从邮件内容中提取到有效的验证码")
            #         code = None
                
            # except Exception as e:
            #     logging.error(f"获取 apiget.com 验证码失败: {str(e)}")
            #     code = None
                
            if not code:
                logging.error("获取验证码失败")
                return False

            logging.info(f"成功获取验证码: {code}")
            logging.info("正在输入验证码...")
            i = 0
            for digit in code:
                tab.ele(f"@data-index={i}").input(digit)
                time.sleep(random.uniform(0.1, 0.3))
                i += 1
            logging.info("验证码输入完成")
            time.sleep(random.uniform(3, 5))
            # 如果出现 server error 则刷新页面重新输入验证码
            if tab.ele("Server Error"):
                logging.error("出现 server error 错误，刷新页面重新输入验证码")
                tab.refresh()
                time.sleep(random.uniform(3, 5))
                tab.ele(f"@data-index={i}").input(digit)
            break
        except Exception as e:
            logging.error(f"验证码处理过程出错: {str(e)}")
            retry_count += 1
            if retry_count >= 1:
                logging.error("已尝试1次获取验证码失败，退出循环")
                return False
        finally:
            if browser_email_manager:
                browser_email_manager.quit_email()
                logging.info("邮件浏览器已关闭...") 
        

    # handle_turnstile(tab)

    wait_time = random.randint(6, 8)
    for i in range(wait_time):
        logging.info(f"等待系统处理中... 剩余 {wait_time-i} 秒")
        time.sleep(1)

    # logging.info("正在获取账户信息...")
    # tab.get(settings_url)
    # try:
    #     usage_selector = (
    #         "css:div.col-span-2 > div > div > div > div > "
    #         "div:nth-child(1) > div.flex.items-center.justify-between.gap-2 > "
    #         "span.font-mono.text-sm\\/\\[0\\.875rem\\]"
    #     )
    #     usage_ele = tab.ele(usage_selector)
    #     if usage_ele:
    #         usage_info = usage_ele.text
    #         total_usage = usage_info.split("/")[-1].strip()
    #         logging.info(f"账户可用额度上限: {total_usage}")
    # except Exception as e:
    #     logging.error(f"获取账户额度信息失败: {str(e)}")

    logging.info("\n=== 注册完成 ===")
    account_info = f"Cursor 账号信息:\n邮箱: {email}\n密码: {password}"
    logging.info(account_info)
    return True


class EmailGenerator:
    def __init__(
        self,
        password="".join(
            random.choices(
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*",
                k=12,
            )
        ),
    ):

        self.default_password = password
        self.default_first_name = self.generate_random_name()
        self.default_last_name = self.generate_random_name()

    def generate_random_name(self, length=6):
        """生成随机用户名"""
        first_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        rest_letters = "".join(
            random.choices("abcdefghijklmnopqrstuvwxyz", k=length - 1)
        )
        return first_letter + rest_letters

    def generate_email(self, length=8):
        """生成随机邮箱地址"""
        random_str = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=length))
        timestamp = str(int(time.time()))[-6:]  # 使用时间戳后6位
        return f"{random_str}{timestamp}@{self.domain}"

    def get_account_info(self):
        """获取完整的账号信息"""
        return {
            "email": self.generate_email(),
            "password": self.default_password,
            "first_name": self.default_first_name,
            "last_name": self.default_last_name,
        }


def generate_random_name(self, length=6):
        """生成随机用户名"""
        first_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        rest_letters = "".join(
            random.choices("abcdefghijklmnopqrstuvwxyz", k=length - 1)
        )
        return first_letter + rest_letters

def get_available_emails(limit=1):
    """获取可用的邮箱账号信息，并将获取到的记录标记为已使用"""
    connection = None
    try:
        # 连接到MySQL数据库
        connection = pymysql.connect(
            host='47.113.188.124',
            port=3306,
            database='cursor',
            user='root',
            password='198811hndx'
        )

        with connection.cursor() as cursor:
            # 查询数据的SQL语句
            select_query = """
            SELECT email, password, client_id, refresh_token, get_email_type
            FROM cursor_email_info 
            WHERE use_status = 0 AND valid_status = 1 
            LIMIT %s
            FOR UPDATE
            """
            # 执行查询操作
            cursor.execute(select_query, (limit,))
            # 获取查询结果
            results = cursor.fetchall()

            # 将结果转换为字典列表
            emails = []
            for row in results:
                email_info = {
                    'email': row[0],
                    'password': row[1], 
                    'client_id': row[2],
                    'refresh_token': row[3],
                    'get_email_type': row[4]
                }
                emails.append(email_info)

            # 更新使用状态
            if emails:
                update_query = """
                UPDATE cursor_email_info 
                SET use_status = 1, 
                    update_time = NOW()
                WHERE email IN (%s)
                """
                format_strings = ','.join(['%s'] * len(emails))
                cursor.execute(update_query % format_strings, 
                             [email['email'] for email in emails])
                connection.commit()
                print(f"Successfully retrieved and updated {len(emails)} email accounts.")
            return emails

    except Exception as e:
        print(f"Error: {e}")
        if connection:
            connection.rollback()
        return []
    finally:
        if connection:
            connection.close()
            print("MySQL connection is closed.")

def generate_random_name(self, length=6):
        """生成随机用户名"""
        first_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        rest_letters = "".join(
            random.choices("abcdefghijklmnopqrstuvwxyz", k=length - 1)
        )
        return first_letter + rest_letters

def update_email_use_status(email, use_status):
    """更新邮箱使用状态"""
    connection = None
    try:
        # 连接到MySQL数据库
        connection = pymysql.connect(
            host='47.113.188.124',
            port=3306,
            database='cursor',
            user='root',
            password='198811hndx'
        )

        with connection.cursor() as cursor:
            # 更新使用状态
            update_query = """
            UPDATE cursor_email_info 
            SET use_status = %s, 
                update_time = NOW()
            WHERE email = %s
            """
            cursor.execute(update_query, (use_status, email))
            connection.commit()
            print(f"Successfully updated email use status to {use_status} for email: {email}")
    except Exception as e:
        print(f"Error: {e}")
        if connection:
            connection.rollback()
    finally:
        if connection:
            connection.close()
            print("MySQL connection is closed.")
            
def save_token_and_email(cursor_token, cursor_email, cursor_email_password, cursor_password, cursor_name, expires_time, cursor_user_sub=None):
    connection = None
    try:
        # 连接到MySQL数据库
        connection = pymysql.connect(
            host='47.113.188.124',
            port=3306,
            database='cursor',
            user='root',
            password='198811hndx'
        )

        with connection.cursor() as cursor:
            # 插入数据的SQL语句
            insert_query = """
            INSERT INTO cursor_token_info (cursor_token, cursor_email, cursor_password, cursor_email_password, cursor_name, expires_time, cursor_user_sub)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            # 执行插入操作
            cursor.execute(insert_query, (cursor_token, cursor_email, cursor_password, cursor_email_password, cursor_name, expires_time, cursor_user_sub))
            # 提交事务
            connection.commit()

        logging.info("Token and email saved successfully.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()
            print("MySQL connection is closed.")

def get_user_agent():
    """获取user_agent"""
    try:
        # 使用JavaScript获取user agent
        browser_manager = BrowserManager()
        browser = browser_manager.init_browser()
        user_agent = browser.latest_tab.run_js("return navigator.userAgent")
        browser_manager.quit()
        return user_agent
    except Exception as e:
        logging.error(f"获取user agent失败: {str(e)}")
        return None


def check_cursor_version():
    """检查cursor版本"""
    pkg_path, main_path = patch_cursor_get_machine_id.get_cursor_paths()
    with open(pkg_path, "r", encoding="utf-8") as f:
        version = json.load(f)["version"]
    return patch_cursor_get_machine_id.version_check(version, min_version="0.45.0")


def reset_machine_id(greater_than_0_45):
    if greater_than_0_45:
        # 提示请手动执行脚本 https://github.com/chengazhen/cursor-auto-free/blob/main/patch_cursor_get_machine_id.py
        go_cursor_help.go_cursor_help()
    else:
        MachineIDResetter().reset_machine_ids()


def print_end_message():
    logging.info("\n\n\n\n\n")
    logging.info("=" * 30)
    logging.info("所有操作已完成")
    logging.info("\n=== 获取更多信息 ===")
    logging.info("🔥 QQ交流群: 1034718338")
    logging.info("📺 B站UP主: 想回家的前端")
    logging.info("=" * 30)

def get_mac_user_agent():
    """获取Mac OS的用户代理字符串"""
    ua = UserAgent()
    while True:
        agent = ua.chrome
        if "Macintosh" in agent:
            return agent
        else:
            continue

 # 获取已授权IP
def delete_auth_id():
    response = requests.get(
        "https://proxy.webshare.io/api/v2/proxy/ipauthorization/",
        headers={"Authorization": "Token 8c3zvexvw5ifyk6ai93vvlfljnmbknhdepq52kar"}
    )
    logging.info(f"已授权IP: {response.json()}")
    
    # 从响应中获取第一个授权ID
    auth_id = None
    try:
        auth_id = response.json()['results'][0]['id']
        logging.info(f"获取到授权ID: {auth_id}")
    except (KeyError, IndexError) as e:
        logging.error(f"获取授权ID失败: {str(e)}")
        auth_id = None

    # 删除授权IP
    if auth_id:
        response = requests.delete(
            f"https://proxy.webshare.io/api/v2/proxy/ipauthorization/{auth_id}/",
            headers={"Authorization": "Token 8c3zvexvw5ifyk6ai93vvlfljnmbknhdepq52kar"}
        )
        logging.info(f"删除授权ID: {auth_id}")

def authorize_current_ip():
    """获取当前IP并进行授权"""
    current_ip = None
    try:
        ip_response = requests.get('https://api.ipify.org')
        if ip_response.status_code == 200:
            current_ip = ip_response.text
            logging.info(f"当前IP地址: {current_ip}")
        else:
            logging.warning("无法获取当前IP地址")
    except Exception as e:
        logging.error(f"获取IP地址时出错: {str(e)}")
        current_ip = None

    # 授权IP
    response = requests.post(
        "https://proxy.webshare.io/api/v2/proxy/ipauthorization/",
        json={"ip_address": current_ip},
        headers={"Authorization": "Token 8c3zvexvw5ifyk6ai93vvlfljnmbknhdepq52kar"})
    
    logging.warning(f"IP授权设置结果: {response.json()}")

if __name__ == "__main__":
    print_logo()
    # greater_than_0_45 = check_cursor_version()
    browser_manager = None
    try:
        logging.info("\n=== 初始化程序 ===")

        logging.info("正在初始化浏览器...")

        if os.getenv('GITHUB_ACTIONS') == 'true':
            # 删除已授权IP
            delete_auth_id()
            # 授权当前IP
            authorize_current_ip()

        logging.info("正在初始化邮箱验证模块...")
        email_handler = EmailVerificationHandler()
        logging.info("\n=== 配置信息 ===")
        login_url = "https://authenticator.cursor.sh"
        sign_up_url = "https://authenticator.cursor.sh/sign-up"
        settings_url = "https://www.cursor.com/settings"
        mail_url = "https://tempmail.plus"


        email_generator = EmailGenerator()
        
        while True:
            
            try:

                emails = get_available_emails()
                if not emails:
                    logging.info("未找到可用的邮箱。等待5分钟后重试...")
                    time.sleep(300)
                    continue
                for email_info in emails:
                    # 打印循环开始时间
                    start_time = time.time()
                    logging.info(f"循环开始时间: {datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')}")
                    email = email_info['email']
                    email_password = email_info['password']
                    client_id = email_info['client_id'] 
                    refresh_token = email_info['refresh_token']
                    get_email_type = email_info['get_email_type']
                    try:
                        password="".join(
                                        random.choices(
                                            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*",
                                            k=12,
                                        )
                                    )
                        first_name = email_generator.generate_random_name()
                        last_name = email_generator.generate_random_name()

                        logging.info(f"从数据库得到邮箱账号: {email}")
                        auto_update_cursor_auth = True

                        browser_manager = BrowserManager()
                        browser = browser_manager.init_browser()

                        tab = browser.latest_tab

                        tab.run_js("try { turnstile.reset() } catch(e) { }")

                        # 获取browser_manager设置的代理IP
                        proxy_ip = browser_manager.proxy_manager.proxy_ip
                        logging.info(f"获取到邮件请求代理IP: {proxy_ip}")

                        logging.info("\n=== 开始注册流程 ===")
                        logging.info(f"正在访问登录页面: {login_url}")
                        tab.get(login_url)
                        

                        logging.info(f"browser_manager的proxy_ip: {proxy_ip}")
                        if sign_up_account(browser_manager, tab, email, email_password, client_id, refresh_token, get_email_type, proxy_ip):
                            logging.info("正在获取会话令牌...")
                            token = get_cursor_session_token(tab, browser_manager)
                            # 计算过期时间
                            expires_time = datetime.now() + timedelta(days=12, hours=23, minutes=59)
                            # token email 保存到数据库表
                            logging.info("正在保存数据库...")
                            save_token_and_email(token, email, email_password, password, f"{first_name} {last_name}", expires_time.strftime('%Y-%m-%d %H:%M:%S'), None)
              
                    finally:
                        if browser_manager:
                            browser_manager.quit()
                            logging.info("浏览器已关闭...")
                        # 计算循环结束时间
                        end_time = time.time()
                        logging.info(f"循环结束时间: {datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')}")
                        # 计算循环时长
                        loop_duration = end_time - start_time
                        logging.info(f"循环时长: {loop_duration} 秒")
                    continue
            except Exception as e:
                print(f"Error getting input: {e}")
                continue
        
    except Exception as e:
        logging.error(f"程序执行出现错误: {str(e)}")
        import traceback

        logging.error(traceback.format_exc())
    finally:
        if browser_manager:
            browser_manager.quit()
        input("\n程序执行完毕，按回车键退出...")
