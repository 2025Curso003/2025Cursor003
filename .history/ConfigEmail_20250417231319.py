class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [



    ("vrtuxqm8358@outlook.com", "ZU0X6xujUf8QG"),
    ("uzfufcqfaq1320@outlook.com", "i0lEFWCEiUW"),

     ("ukvhnxxreg802@outlook.com", "8SdIcSHzdEXsi"),
    ("kqcizrjoeq0639@outlook.com", "YOpD5XRx9sZb")


            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)