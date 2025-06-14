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
                
                # 关闭旧的浏览器
                self.browser.quit()
                
                # 创建新的浏览器选项
                co = ChromiumOptions()
                co.set_argument(f'--proxy-server={proxy}')
                co.set_argument('--incognito')  # 启用隐私模式
                co.set_argument('--disable-blink-features=AutomationControlled')
                co.set_argument('--no-sandbox')
                co.set_argument('--disable-gpu')
                co.set_argument('--lang=en-US,en')
                co.set_argument('--disable-extensions')  # 禁用扩展
                co.set_argument('--disable-default-apps')
                  # 禁用默认应用
                co.auto_port = True
                
                # 创建新的浏览器实例
                self.browser = Chromium(co)
                logging.info(f"成功切换到新代理: {proxy}")
                return True
        except Exception as e:
            logging.error(f"切换代理失败: {e}")
        return False

    def init_browser(self, user_agent=None):
        """初始化浏览器"""
       
        co = self._get_browser_options(user_agent)
        co.headless(False)  # 设置为 False 显示浏览器
        
        co.set_argument('--window-position=-9999,-9999')  # 将窗口移出屏幕
        co.set_argument('--window-size=800,600')  # 设置窗口大小  # 禁用默认应用
        
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
        proxy = self.proxy_manager.get_proxy_pool()
        logging.info(f"使用代理ip: {proxy}")
        if proxy:
            co.set_proxy(proxy)

        co.auto_port()
        if user_agent:
            co.set_user_agent(user_agent)

        co.headless(
            os.getenv("BROWSER_HEADLESS", "True").lower() == "true"
        )  # 生产环境使用无头模式

        # Mac 系统特殊处理
        if sys.platform == "darwin":
            # co.set_argument("--no-sandbox")
            co.set_argument("--disable-gpu")

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
