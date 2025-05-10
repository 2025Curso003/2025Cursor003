from DrissionPage import ChromiumOptions, Chromium
import sys
import os
import logging
from dotenv import load_dotenv

from proxy_manager import ProxyManager

load_dotenv()


class BrowserManager:
    def __init__(self):
        self.proxy_manager = ProxyManager()
        self.browser = None

    def switch_proxy(self):
        """切换到新的代理"""
        try:
            proxy = self.proxy_manager.get_proxy_pool()
            if proxy and self.browser:
                logging.info(f"准备切换到新代理: {proxy}")
                
                # 保存当前浏览器的cookies
                old_cookies = self.browser.get_cookies()
                logging.info("已保存当前浏览器cookies")
                
                # 保存当前URL
                current_url = self.browser.latest_tab.url
                logging.info(f"当前页面URL: {current_url}")
                
                # 关闭旧的浏览器
                self.browser.quit()
                
                # 创建新的浏览器选项
                co = self._get_browser_options()
                co.set_proxy(proxy)  # 设置新代理
                
                # 创建新的浏览器实例
                self.browser = Chromium(co)
                
                # 恢复到之前的页面
                self.browser.latest_tab.get(current_url)
                
                # 恢复之前的cookies
                for cookie in old_cookies:
                    self.browser.latest_tab.set_cookies(cookie)
                logging.info("已恢复之前的cookies")
                
                logging.info(f"成功切换到新代理: {proxy}")
                return True
            return False
        except Exception as e:
            logging.error(f"切换代理失败: {e}")
            return False

    def init_browser(self, user_agent=None):
        """初始化浏览器"""
        co = self._get_browser_options(user_agent)
        self.browser = Chromium(co)
        return self.browser

    def _get_browser_options(self, user_agent=None):
        """获取浏览器配置"""
        co = ChromiumOptions()
        try:
            extension_path = self._get_extension_path()
            co.add_extension(extension_path)
        except FileNotFoundError as e:
            logging.warning(f"警告: {e}")

        co.set_pref("credentials_enable_service", False)
        co.set_argument("--hide-crash-restore-bubble")
        
        # 设置代理
        proxy = self.proxy_manager.get_proxy_pool()
        logging.info(f"使用代理ip: {proxy}")
        if proxy:
            co.set_proxy(proxy)

        # 设置端口
        co.auto_port()

        # 设置 User-Agent
        if user_agent:
            co.set_user_agent(user_agent)

        if os.getenv('GITHUB_ACTIONS') == 'true':
            co.set_user_agent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        # 设置无头模式
        is_headless = os.getenv("CHROME_ARGS", "").find("--headless=new") != -1
        co.headless(is_headless)

        # 添加必要的启动参数
        chrome_args = os.getenv("CHROME_ARGS", "").split()
        for arg in chrome_args:
            if arg:
                co.set_argument(arg)

        # GitHub Actions 环境特殊配置
        if os.getenv('GITHUB_ACTIONS'):
            co.set_argument('--no-sandbox')
            co.set_argument('--disable-dev-shm-usage')
            co.set_argument('--disable-gpu')
            co.headless(True)
        else:
            co.headless(False)

        if os.getenv('GITHUB_ACTIONS'):
            co.set_argument('--no-sandbox')
            co.set_argument('--disable-dev-shm-usage')
            co.set_argument('--disable-gpu')
            co.headless(True)
        else:
            co.headless(False)

        # 设置窗口大小
        co.set_argument('--window-size=800,600')

        co.set_argument('--disable-blink-features=AutomationControlled')
        # co.set_argument('--disable-web-security')
        co.set_argument('--allow-running-insecure-content')
        co.set_argument('--disable-features=IsolateOrigins,site-per-process')
        co.set_argument('--ignore-certificate-errors') 
        return co

    def _get_extension_path(self):
        """获取插件路径"""
        root_dir = os.getcwd()
        extension_path = os.path.join(root_dir, "turnstilePatch")

        if hasattr(sys, "_MEIPASS"):
            extension_path = os.path.join(sys._MEIPASS, "turnstilePatch")

        if not os.path.exists(extension_path):
            raise FileNotFoundError(f"插件不存在: {extension_path}")

        return extension_path

    def quit(self):
        """关闭浏览器"""
        if self.browser:
            try:
                self.browser.quit()
            except:
                pass
