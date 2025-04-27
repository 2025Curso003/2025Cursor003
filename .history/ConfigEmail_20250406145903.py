class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

               
                ("tbgobusqn5@outlook.com", "che860371"),
                ("lqzxuue285@outlook.com", "xpa316070"),
                ("zwswntg08@outlook.com", "utg198544"),
                ("rrpvcjcl8@outlook.com", "kxg984331"),
                ("ewskdujt1@outlook.com", "xcq073812"),
                ("gtlahfe76@outlook.com", "qrf192955"),
                ("knurrraw730@outlook.com", "ini527922"),
                ("zfbyhstupb25@outlook.com", "hnu604783"),
                ("jvqgcvz026@outlook.com", "slq001674"),
                ("pinnzbocum981@outlook.com", "whu613017")          

            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)