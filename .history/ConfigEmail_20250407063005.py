class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

# ("vaocnfl0@outlook.com", "ugh574844"),
# ("kvpucde8@outlook.com", "czf543817"),
# ("xxzygbwf2@outlook.com", "wla252805"),
# ("upgojnsutn50@outlook.com", "jzt419910"),
# ("mjlyoyuuj76@outlook.com", "cnr574335"),
# ("ahwulogalc5@outlook.com", "fld702419"),
# ("ekehjvms65@outlook.com", "zrh047757"),
# ("lqinbwnvsb55@outlook.com", "avl398837"),

# ("hpbihdkmu4@outlook.com", "owx855860"), 
# ("cydjewlkbr29@outlook.com", "bwm681746"),
#  ("ktckbmgjy3@outlook.com", "nee191171"), 
#  ("wgbbpgkqx3@outlook.com", "eit688535")


("sfu7150992953@163.com", "kiffm3098"),
            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)