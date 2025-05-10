import requests
import logging
import os
class ProxyManager:
    def __init__(self):
        # 代理池列表，可以从文件或API获取
        self.proxy_pool = []
        self.proxy_ip = None
        
    def get_proxy_pool(self):
        """随机获取一个代理"""
        # 检查是否在 GitHub Actions 环境中运行
        # if os.getenv('GITHUB_ACTIONS') == 'true':
        #     logging.info("在 GitHub Actions 环境中运行，不使用代理")
        #     return None
            

        try:
            # api_url = "https://api.hailiangip.com:8522/api/getIpEncrypt?dataType=1&encryptParam=SlDyzgfgDW12vuaMHmQkM1l3svlLMXCHw0IlSHvOue3lVhShpdEjb9vG2YRiwpyEPcEigFrowb8LwrKtIDRCi2nxZO4gzU%2FNBKc7dcEloB6dRtYN%2FWLh1y5OUBVBECwLaba73pX8g9o%2BOwUVVgZXqClj3XytwbUPdk0POJVVN4HYFsJvJYxeLU9YDql4IJq6KHmQBjYm32MK13MpScW7XN0Jv%2FQlqwlcd4gkrYI6AFg%3D"
            # 这里替换为您的代理API地址
            # 快代理
            # api_url = "https://dps.kdlapi.com/api/getdps/?secret_id=o2zs8dtoterr839x54kr&signature=1aocu0ztzt3u6buib0s69s6ts71eeafu&num=1&pt=1&format=text&sep=1"
            # 51代理送20元但是流量不行
            # api_url = "http://bapi.51daili.com/getapi2?linePoolIndex=3&packid=2&time=32&qty=1&port=1&format=txt&dt=2&usertype=17&uid=57621"
            # 卓越代理限制3分钟流量可以
            # api_url = "http://zhuoyuekeji.zhuoyuejituan.com:66/SML.aspx?action=GetIP&OrderNumber=c96ca54b71b9597eb7da08a370803422&isp=&poolnumber=0&AuthMode=0&UserName=zf772835869@88.com&UserPwd=q1w2e3r4&RangeNumber=0&Split=&Address=&qty=1"
            # api_url = "http://api.shenlongip.com/ip?key=m36pvt0c&protocol=1&mr=1&pattern=txt&count=1&sign=2b8a1c6f446251113e5ffdace90827b3"
            # 海外代理 试用中
            api_url = "https://api.haiwaidaili.net/abroad?token=a54cd531a3dad7ce364bcc2f92cba110&num=1&format=1&protocol=http&country=&state=&city=&sep=1&csep=&area="
            logging.info(f"获取代理ip成功: {api_url}")
            response = requests.get(api_url)
            
            if response.status_code == 200:
                logging.info(f"获取代理ip成功: {response.text}")
                self.proxy_ip = response.text
                return response.text;
        except Exception as e:
            logging.error(f"获取代理ip失败: {e}")
            return None