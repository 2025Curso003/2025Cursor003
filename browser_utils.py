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
                logging.info("使用无认证代理")
            except Exception as e:
                logging.error(f"设置代理时出错: {e}")

        # 检测运行环境
        is_linux = sys.platform.startswith('linux')
        is_github_actions = os.getenv('GITHUB_ACTIONS') == 'true'
        
        # 基本配置（适用于所有环境）
        co.set_argument('--no-sandbox')  # 添加到所有环境
        co.set_argument('--disable-dev-shm-usage')
        co.set_argument('--disable-gpu')
        co.set_argument('--disable-software-rasterizer')
        co.set_argument('--ignore-certificate-errors')
        co.set_argument('--disable-web-security')
        
        # 在 Linux 或 GitHub Actions 环境下的特殊配置
        if is_linux or is_github_actions:
            co.set_argument('--headless=new')
            co.set_user_agent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
            
            # 其他 Linux 特定配置保持不变
            # 临时文件目录
            co.set_argument("--disk-cache-dir=/tmp/chrome-cache")
            
            # GPU 相关配置
            co.set_argument('--disable-gpu-compositing')  # 禁用GPU合成
            co.set_argument('--disable-gpu-rasterization')  # 禁用GPU光栅化
            co.set_argument('--disable-3d-apis')  # 禁用3D APIs
            co.set_argument('--disable-accelerated-2d-canvas')  # 禁用加速2D画布
            co.set_argument('--disable-accelerated-video-decode')  # 禁用视频解码加速
            co.set_argument('--disable-accelerated-video-encode')  # 禁用视频编码加速
            
            # SSL 配置
            co.set_argument('--allow-insecure-localhost')
            co.set_argument('--disable-web-security')
            co.set_argument('--reduce-security-for-testing')  # 仅用于测试环境
            
            # 内存优化
            co.set_argument('--disable-extensions')  # 禁用扩展
            co.set_argument('--disable-dev-tools')  # 禁用开发者工具
            co.set_argument('--disable-browser-side-navigation')  # 禁用浏览器端导航
            co.set_argument('--disable-infobars')  # 禁用信息栏
            
            # 性能优化
            co.set_argument('--disable-backgrounding-occluded-windows')  # 禁用后台窗口
            co.set_argument('--disable-renderer-backgrounding')  # 禁用渲染器后台处理
            co.set_argument('--disable-background-timer-throttling')  # 禁用后台计时器限制
            
            # 安全和稳定性
            co.set_argument('--disable-translate')  # 禁用翻译
            co.set_argument('--disable-sync')  # 禁用同步
            co.set_argument('--disable-default-apps')  # 禁用默认应用
            co.set_argument('--disable-prompt-on-repost')  # 禁用重新发布提示
            co.set_argument('--disable-domain-reliability')  # 禁用域可靠性监控
            
            # 调试和日志
            co.set_argument('--enable-logging')  # 启用日志
            co.set_argument('--v=1')  # 详细日志级别
            co.set_argument('--log-level=0')  # 设置日志级别
            
            logging.info("在Linux/GitHub Actions环境下运行，使用无头模式")
        else:
            co.headless(False)
            logging.info("在其他环境下运行，使用有界面模式")

        # 设置固定的调试端口
        import random
        debug_port = random.randint(9222, 9999)
        co.set_argument(f'--remote-debugging-port={debug_port}')
        logging.info(f"设置调试端口: {debug_port}")
        
        # 设置窗口大小
        co.set_argument('--window-size=1280,800')

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
