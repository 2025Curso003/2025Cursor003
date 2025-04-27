class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [



("duntzbillij6@outlook.com","VDoo9npz"),
("britoelhamx1@outlook.com","ellEOd2K"),
("weidatireyt2@outlook.com","xYFo2OUB")
            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)