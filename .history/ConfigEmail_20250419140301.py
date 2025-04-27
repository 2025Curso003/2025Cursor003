class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [




        

            
           
            ("xzhbbxmrgz2272@outlook.com", "1iuNUChju"),
            ("ocmwsmsg095@outlook.com", "6QnwUEKkqSj"),
            ("qxefgvetai508@outlook.com", "tmbG7wFLayg8z"),
            ("zwigfofja9086@outlook.com", "odnbjbb7uM2"),
            ("smswsdut5175@outlook.com", "97I8rTYI3DHV"),
            ("yvhxovttdo453@outlook.com", "0W2lAcU6SbAT"),
            ("hrbvhhrmwz515@outlook.com", "bHlMQk8fd0V")


            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)