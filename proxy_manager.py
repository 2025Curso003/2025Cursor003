import requests
import logging
import os
import random
import sys

class ProxyManager:
    def __init__(self):
        # 代理池列表，可以从文件或API获取
        self.proxy_pool = []
        self.proxy_ip = None
        # Webshare API 配置
        self.webshare_api_key = os.getenv('WEBSHARE_API_KEY', 't7lkf1rmu3rvr154l73yp387lmyf8m7xd8b8v2hj')  # 从环境变量获取API密钥
        self.webshare_proxy_list = []
        self.proxy_auth_list = []  # 存储认证信息
        
    def get_webshare_proxy(self):
        """获取 Webshare 代理"""
        try:
            # 获取代理列表
            api_url = "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=100"
            headers = {
                "Authorization": f"Token {self.webshare_api_key}",
                "Accept": "application/json"
            }
            
            logging.info(f"正在请求 Webshare API: {api_url}")
            response = requests.get(api_url, headers=headers)
            logging.info(f"API 响应状态码: {response.status_code}")
            
            if response.status_code == 200:
                proxy_data = response.json()
                logging.debug(f"API 响应数据: {proxy_data}")
                self.webshare_proxy_list = []
                self.proxy_auth_list = []  # 清空认证信息列表
                
                results = proxy_data.get('results', [])
                logging.info(f"获取到 {len(results)} 个代理")
                
                for proxy in results:
                    try:
                        # 记录原始代理数据用于调试
                        logging.debug(f"处理代理数据: {proxy}")
                        
                        # 构建代理地址和认证信息
                        proxy_address = f"{proxy['proxy_address']}:{proxy['port']}"
                        auth_info = f"{proxy['username']}:{proxy['password']}"
                        
                        self.webshare_proxy_list.append(proxy_address)
                        self.proxy_auth_list.append(auth_info)
                        logging.debug(f"成功添加代理: {proxy_address}")
                    except KeyError as e:
                        logging.error(f"代理数据缺少必要字段 {e}, 完整数据: {proxy}")
                        continue
                
                if self.webshare_proxy_list:
                    # 随机选择一个代理和对应的认证信息
                    index = random.randint(0, len(self.webshare_proxy_list) - 1)
                    selected_proxy = self.webshare_proxy_list[index]
                    self.current_auth = self.proxy_auth_list[index]
                    logging.info(f"成功获取 Webshare 代理: {selected_proxy}")
                    return selected_proxy
                else:
                    logging.error("没有可用的代理")
                    return None
                    
            logging.error(f"获取 Webshare 代理失败，状态码: {response.status_code}")
            if response.status_code != 200:
                logging.error(f"错误响应内容: {response.text}")
            return None
            
        except Exception as e:
            logging.error(f"获取 Webshare 代理出错: {str(e)}")
            logging.exception("详细错误信息:")
            return None
        
    def get_proxy_pool(self):
        """获取代理"""
        try:
            # 如果 Webshare 不可用，使用备用代理
            # 如果是linux系统
            if sys.platform.startswith('linux') or os.getenv('GITHUB_ACTIONS') == 'true':
                # 海外代理
                # 优先使用 Webshare 代理
                proxy = self.get_webshare_proxy()
                if proxy:
                    self.proxy_ip = proxy
                    return proxy
            else:
                # api_url = "https://api.hailiangip.com:8522/api/getIpEncrypt?dataType=1&encryptParam=SlDyzgfgDW12vuaMHmQkM1l3svlLMXCHw0IlSHvOue3lVhShpdEjb9vG2YRiwpyEPcEigFrowb8LwrKtIDRCi2nxZO4gzU%2FNBKc7dcEloB6dRtYN%2FWLh1y5OUBVBECwLaba73pX8g9o%2BOwUVVgZXqClj3XytwbUPdk0POJVVN4HYFsJvJYxeLU9YDql4IJq6KHmQBjYm32MK13MpScW7XN0Jv%2FQlqwlcd4gkrYI6AFg%3D"
                # 这里替换为您的代理API地址
                # 快代理
                # api_url = "https://dps.kdlapi.com/api/getdps/?secret_id=o2zs8dtoterr839x54kr&signature=1aocu0ztzt3u6buib0s69s6ts71eeafu&num=1&pt=1&format=text&sep=1"
                # 51代理送20元但是流量不行
                # api_url = "http://bapi.51daili.com/getapi2?linePoolIndex=3&packid=2&time=32&qty=1&port=1&format=txt&dt=2&usertype=17&uid=57621"
                # 海外代理 试用中
                # api_url = "https://api.haiwaidaili.net/abroad?token=a54cd531a3dad7ce364bcc2f92cba110&num=1&format=1&protocol=http&country=&state=&city=&sep=1&csep=&area="
                # 卓越代理
                api_url = "http://zhuoyuekeji.zhuoyuejituan.com:66/SML.aspx?action=GetIP&OrderNumber=c96ca54b71b9597eb7da08a370803422&isp=&poolnumber=0&AuthMode=0&UserName=zf772835869@88.com&UserPwd=q1w2e3r4&RangeNumber=0&Split=&Address=&qty=1"
                logging.info("使用卓越代理")
            
            logging.info(f"正在获取代理IP: {api_url}")
            response = requests.get(api_url)
            
            if response.status_code == 200:
                self.proxy_ip = response.text.strip()
                logging.info(f"成功获取代理IP: {self.proxy_ip}")
                return self.proxy_ip
                
        except Exception as e:
            logging.error(f"获取代理失败: {e}")
            return None
            
    def test_proxy(self, proxy):
        """测试代理是否可用"""
        try:
            test_url = "https://api.webshare.io/api/v2/ip-authorization/whatsmyip/"
            proxies = {
                "http": proxy,
                "https": proxy
            }
            response = requests.get(test_url, proxies=proxies, timeout=10)
            if response.status_code == 200:
                ip_info = response.json()
                logging.info(f"代理测试成功，IP信息: {ip_info}")
                return True
            return False
        except Exception as e:
            logging.error(f"代理测试失败: {e}")
            return False