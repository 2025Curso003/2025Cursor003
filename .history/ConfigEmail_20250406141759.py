class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

               
                
("fefsmdyb12@outlook.com", "ecb188314"),  
("pveeccsqhc554@outlook.com", "eeh596126"),  
("wafxvpkmmp376@outlook.com", "nxs307968"),  
("squreocs521@outlook.com", "epp923583"),  
("qurhxbf2@outlook.com", "npc160904"),  
("fxoehrfgmh450@outlook.com", "bxu272107"),  
("adfcdc6516@outlook.com", "aec880777"),  
("crxymqwe188@outlook.com", "jvd565769"),  
("vvwqsjut947@outlook.com", "cax684439"),  
("emukwiobp9@outlook.com", "wvm082978")

              

            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)