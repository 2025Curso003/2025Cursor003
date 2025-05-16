from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from proxy_manager import ProxyManager
import logging
import threading
import os
import platform

class BrowserManager:
    def __init__(self):
        self.proxy_manager = ProxyManager()
        self._browser = None

    def init_browser(self):
        """初始化浏览器实例"""
        try:
            # 获取代理
            proxy_info = self.proxy_manager.get_random_proxy()
            if not proxy_info:
                logging.error("无法获取代理")
                return None

            # 设置Chrome选项
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('--disable-software-rasterizer')

            # 设置代理
            proxy_str = f"{proxy_info['proxy_address']}:{proxy_info['port']}"
            chrome_options.add_argument(f'--proxy-server={proxy_str}')

            # 在macOS上指定Chrome二进制文件路径
            if platform.system() == 'Darwin':
                chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

            # 创建浏览器实例
            self._browser = webdriver.Chrome(options=chrome_options)

            # 设置代理认证
            self._browser.execute_cdp_cmd('Network.enable', {})
            self._browser.execute_cdp_cmd('Network.setExtraHTTPHeaders', {
                'headers': {
                    'Proxy-Authorization': f'Basic {self._get_proxy_auth_header(proxy_info)}'
                }
            })

            logging.info(f"浏览器初始化成功，使用代理: {proxy_str}")
            return self._browser

        except Exception as e:
            logging.error(f"初始化浏览器失败: {e}")
            if self._browser:
                self._browser.quit()
            return None

    def _get_proxy_auth_header(self, proxy_info):
        """生成代理认证头"""
        import base64
        auth_str = f"{proxy_info['username']}:{proxy_info['password']}"
        return base64.b64encode(auth_str.encode()).decode()

    def quit(self):
        """关闭浏览器"""
        if self._browser:
            try:
                self._browser.quit()
                logging.info("浏览器已关闭")
            except Exception as e:
                logging.error(f"关闭浏览器时出错: {e}")
            finally:
                self._browser = None