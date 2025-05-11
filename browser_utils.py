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
        logging.info("日志1")
        is_linux = sys.platform.startswith('linux')
        logging.info("日志2")
        is_github_actions = os.getenv('GITHUB_ACTIONS') == 'true'
        logging.info("日志3")
        # 基本配置（适用于所有环境）
        co.set_argument('--disable-dev-shm-usage')
        co.set_argument('--disable-gpu')
        # co.set_argument('--ignore-certificate-errors')
       
        logging.info("日志4")
        # 在 Linux 或 GitHub Actions 环境下的特殊配置
        if is_linux or is_github_actions:
            # co.set_argument('--no-sandbox')  # 在 Linux 环境必需
            co.headless(False)
            co.set_user_agent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
            logging.info("日志5")
            # 确保 /tmp 目录存在并有正确权限
            tmp_dirs = ['/tmp/chrome-cache', '/tmp/chrome-user-data']
            for tmp_dir in tmp_dirs:
                if not os.path.exists(tmp_dir):
                    os.makedirs(tmp_dir, mode=0o777, exist_ok=True)
            
            # # 设置缓存目录
            # co.set_argument('--disk-cache-dir=/tmp/chrome-cache')
            
            # # GPU 和渲染相关配置
            # co.set_argument('--disable-gpu-compositing')
            # co.set_argument('--disable-gpu-rasterization')
            # co.set_argument('--disable-3d-apis')
            
            # # SSL 配置
            # co.set_argument('--allow-insecure-localhost')
            # co.set_argument('--disable-web-security')
            # co.set_argument('--reduce-security-for-testing')  # 仅用于测试环境
            
            # # 内存优化
            # co.set_argument('--disable-extensions')  # 禁用扩展
            # co.set_argument('--disable-dev-tools')  # 禁用开发者工具
            # co.set_argument('--disable-browser-side-navigation')  # 禁用浏览器端导航
            # co.set_argument('--disable-infobars')  # 禁用信息栏
            
            # # 性能优化
            # co.set_argument('--disable-backgrounding-occluded-windows')  # 禁用后台窗口
            # co.set_argument('--disable-renderer-backgrounding')  # 禁用渲染器后台处理
            # co.set_argument('--disable-background-timer-throttling')  # 禁用后台计时器限制
            
            # # 安全和稳定性
            # co.set_argument('--disable-translate')  # 禁用翻译
            # co.set_argument('--disable-sync')  # 禁用同步
            # co.set_argument('--disable-default-apps')  # 禁用默认应用
            # co.set_argument('--disable-prompt-on-repost')  # 禁用重新发布提示
            # co.set_argument('--disable-domain-reliability')  # 禁用域可靠性监控
            
            # # 调试和日志
            # co.set_argument('--enable-logging')  # 启用日志
            # co.set_argument('--v=1')  # 详细日志级别
            # co.set_argument('--log-level=0')  # 设置日志级别
            
            # # 重要：启用必要的功能
            # co.set_argument('--enable-javascript')
            # co.set_argument('--enable-webgl')  # Turnstile 可能需要
            # co.set_argument('--enable-web-security')
            co.set_argument('--window-size=1280,800')  # 确保足够的窗口大小
            
            logging.info("在Linux环境下运行，使用无头模式")
        else:
            co.headless(False)
            # 设置窗口大小
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
