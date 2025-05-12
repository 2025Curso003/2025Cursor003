from DrissionPage import ChromiumOptions, Chromium
import sys
import os
import logging
from dotenv import load_dotenv
from proxy_auth_extension import generate_proxy_extension

from proxy_manager import ProxyManager

load_dotenv()


class BrowserManager:
    def __init__(self):
        self.proxy_manager = ProxyManager()
        self.browser = None
        
        # 检查是否在 Linux 环境下
        if sys.platform.startswith('linux'):
            # 设置 DISPLAY 环境变量
            if not os.getenv('DISPLAY'):
                os.environ['DISPLAY'] = ':99'
                logging.info("设置 DISPLAY 环境变量为 :99")
            
            # 检查 Xvfb 是否已启动
            try:
                import subprocess
                subprocess.run(['pgrep', 'Xvfb'], check=True)
                logging.info("检测到 Xvfb 已运行")
            except subprocess.CalledProcessError:
                logging.warning("Xvfb 未运行，尝试启动...")
                try:
                    # 启动 Xvfb
                    subprocess.Popen(['Xvfb', ':99', '-screen', '0', '1280x800x24', '-ac'])
                    logging.info("成功启动 Xvfb")
                except Exception as e:
                    logging.error(f"启动 Xvfb 失败: {e}")

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
        
        # 设置唯一的用户数据目录
        import tempfile
        import uuid
        user_data_dir = os.path.join(tempfile.gettempdir(), f'chrome-user-data-{uuid.uuid4()}')
        os.makedirs(user_data_dir, exist_ok=True)
        co.set_argument(f'--user-data-dir={user_data_dir}')
        
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
            try:
                co.set_proxy(proxy)
                co.set_argument('--proxy-server=' + proxy)
                co.set_argument('--proxy-bypass-list=<-loopback>')
                logging.info("日志0")
                logging.info("使用无认证代理")
            except Exception as e:
                logging.error(f"设置代理时出错: {e}")

        # 检测运行环境
        is_linux = sys.platform.startswith('linux')
        is_github_actions = os.getenv('GITHUB_ACTIONS') == 'true'
        # 基本配置（适用于所有环境）
        co.set_argument('--disable-dev-shm-usage')
        co.set_argument('--disable-gpu')
       
        # 在 Linux 或 GitHub Actions 环境下的特殊配置
        if is_linux or is_github_actions:
            co.headless(False)
            co.set_argument('--window-size=1280,800')  # 确保足够的窗口大小
            logging.info("在Linux环境下运行，使用无头模式")
        else:
            co.headless(False)
            co.set_argument('--window-size=900,800')
            logging.info("在其他环境下运行，使用有界面模式")

        # 设置固定的调试端口
        import random
        debug_port = random.randint(9222, 9999)
        co.set_argument(f'--remote-debugging-port={debug_port}')
        logging.info(f"设置调试端口: {debug_port}")
        
        # 自动化相关
        co.set_argument('--disable-blink-features=AutomationControlled')
        co.set_argument('--allow-running-insecure-content')
        co.set_argument('--disable-features=IsolateOrigins,site-per-process')
        
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