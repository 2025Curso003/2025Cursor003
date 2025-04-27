class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [




("hanomdaduna@hotmail.com", "bAQiqv01"),
("konerudhiva@hotmail.com", "V7b2t032"),
("dedeqrolli@hotmail.com", "0xvcoO41")


            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)