class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

# ("CruzRichard4717@outlook.com", "@aipget.com"),
# ("MillerCheryl9633@outlook.com", "@aipget.com"),
# ("MedinaLaura5066@outlook.com", "@aipget.com"),
# ("DaltonSarah1488@outlook.com", "@aipget.com"),
# ("HudsonMichele1652@outlook.com", "@aipget.com"),
("WebsterDawn8692@outlook.com", "@aipget.com"),
("FisherKimberly4027@outlook.com", "@aipget.com"),
("FosterSavannah1907@outlook.com", "@aipget.com"),
("SmithRichard6498@outlook.com", "@aipget.com"),
("PerezChristian9517@outlook.com", "@aipget.com")

            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)