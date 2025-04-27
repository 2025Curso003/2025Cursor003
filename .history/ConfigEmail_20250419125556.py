class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [




        

            
           
            ("aziftcth618@outlook.com", "qQRFlLZk5NX"),
            ("quhhtunm3064@outlook.com", "JvKbwYxao"),
            ("lcazbqbnt3201@outlook.com", "M5bvNvIUBd5J"),
            # ("rdktynzfrk4146@outlook.com", "cdVD5zqjB"),
            # ("yajhccxo8311@outlook.com", "igHjucAfDBcz"),
            # ("vxudjngeug0276@outlook.com", "5CFSSIO6VZZXt"),
            # ("xaeatwpbq679@outlook.com", "ELqz7prswbTWw"),
            # ("htoltyy526@outlook.com", "r8YKkWPN9tvet"),
            # ("giypjoqdga3531@outlook.com", "thT1HCBZH2"),
            # ("ptvgreqe649@outlook.com", "wwXL1JtNCeEI"),
            # ("uwbzxcyy269@outlook.com", "UnlsDGYfZrUkV"),
            # ("pbpsiaqree6851@outlook.com", "ipUOvJp5I3k5R"),
            # ("xzhbbxmrgz2272@outlook.com", "1iuNUChju"),
            # ("ocmwsmsg095@outlook.com", "6QnwUEKkqSj"),
            # ("qxefgvetai508@outlook.com", "tmbG7wFLayg8z"),
            # ("zwigfofja9086@outlook.com", "odnbjbb7uM2"),
            # ("smswsdut5175@outlook.com", "97I8rTYI3DHV"),
            # ("yvhxovttdo453@outlook.com", "0W2lAcU6SbAT"),
            # ("hrbvhhrmwz515@outlook.com", "bHlMQk8fd0V")


            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)