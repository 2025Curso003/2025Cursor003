class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [


("mayoodqader4@hotmail.com", "@aipget.com"),
("mireslovetim@hotmail.com", "@aipget.com"),
("muziomcann16@hotmail.com", "@aipget.com")
            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)