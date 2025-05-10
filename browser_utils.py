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
        if proxy:
            logging.info(f"使用代理ip: {proxy}")
            # 设置代理服务器
            co.set_proxy(proxy)
            
            # 如果有代理认证信息，添加代理认证扩展
            if hasattr(self.proxy_manager, 'current_auth'):
                auth = self.proxy_manager.current_auth.split(':')
                if len(auth) == 2:
                    username, password = auth
                    co.set_proxy_auth(username, password)
                    logging.info("已设置代理认证信息")

        # 设置端口
        co.auto_port()

        if os.getenv('GITHUB_ACTIONS') == 'true':
            co.set_user_agent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        # GitHub Actions 环境特殊配置
        if os.getenv('GITHUB_ACTIONS'):
            co.set_argument('--no-sandbox')
            co.set_argument('--disable-dev-shm-usage')
            co.set_argument('--disable-gpu')
            co.headless(True)
        else:
            co.headless(False)

        # 设置窗口大小
        co.set_argument('--window-size=1920,1080')

        co.set_argument('--disable-blink-features=AutomationControlled')
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
