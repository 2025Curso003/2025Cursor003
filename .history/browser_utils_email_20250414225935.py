from DrissionPage import ChromiumOptions, Chromium
from DrissionPage import ChromiumPage
import sys
import os
import logging
from dotenv import load_dotenv
from cursor_pro_keep_alive import get_mac_user_agent
from proxy_manager import ProxyManager
load_dotenv()


class BrowserManagerEmail:
    def __init__(self):
        self.proxy_manager = ProxyManager()
        self.browser = None

    def init_browser(self, user_agent=None):
        """初始化浏览器"""
        # 创建浏览器选项
        co = ChromiumOptions()
        # 设置无头模式
        co.headless(False)  # 添加这行来启用无头模式
        # 基本设置
        co.auto_port()
        co.set_argument('--incognito')  # 启用隐私模式
        # co.set_argument('--no-sandbox')
        co.set_argument('--disable-gpu')
        co.set_argument('--lang=en-US,en')
        co.set_argument('--disable-extensions')  # 禁用扩展
        co.set_argument('--disable-default-apps')  # 禁用默认应用
        
        # 设置窗口位置和大小，使其在后台运行
        co.set_argument('--window-position=-9999,-9999')  # 将窗口移出屏幕
        co.set_argument('--window-size=800,600')  # 设置窗口大小
        
        # proxy = self.proxy_manager.get_proxy_pool()
        # logging.info(f"使用代理ip: {proxy}")
        # if proxy:
        #     co.set_proxy(proxy)

        # 设置 User-Agent
        if user_agent:
            co.set_user_agent(user_agent)
        # else:
        #     co.set_user_agent(get_mac_user_agent())
        
        # 创建浏览器实例
        self.browser = ChromiumPage(co)
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
        proxy = os.getenv("BROWSER_PROXY")
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
            co.set_argument("--no-sandbox")
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
        """关闭浏览器并清除缓存"""
        if self.browser:
            try:
                # 清除缓存
                self.browser.clear_cache()  # 清除缓存数据
                self.browser.clear_cookies()  # 清除 cookies
                
                # 关闭浏览器
                self.browser.quit()
                
            except Exception as e:
                logging.error(f"关闭浏览器或清除缓存时出错: {e}")
                # 如果正常关闭失败，尝试强制结束进程
                try:
                    import psutil
                    for proc in psutil.process_iter():
                        try:
                            if "chrome" in proc.name().lower():
                                proc.kill()
                        except:
                            pass
                except:
                    pass
            finally:
                self.browser = None

    def quit_email(self):
        """关闭浏览器"""
        if self.browser:
            try:
                self.browser.quit()
            except:
                pass