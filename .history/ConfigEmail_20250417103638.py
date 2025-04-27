class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [



# ("alornuchevet@hotmail.com", "e9Cv6U80"),

("etukokajino@hotmail.com", "CkCuqQ71"),
("tsimidear@hotmail.com", "8ySGrJ14"),
("hanomdaduna@hotmail.com", ""),
("konerudhiva@hotmail.com", ""),
("dedeqrolli@hotmail.com", ""),


#  ("uimxnajwl12@outlook.com", "boz544735")

            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)