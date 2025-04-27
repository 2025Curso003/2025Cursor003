class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [



# ("alornuchevet@hotmail.com", "e9Cv6U80"),
("koonsbulaja@hotmail.com", "y1Rr2Z66"),
("vsacapra@hotmail.com", "nuaNO884"),
("vovkojucja@hotmail.com", "4OhTEN29"),
("aniiecialin@hotmail.com", "1ASNvC15")


#  ("uimxnajwl12@outlook.com", "boz544735")

            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)