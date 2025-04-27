class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

("vaocnfl0@outlook.com", "ugh574844"),
("kvpucde8@outlook.com", "czf543817"),
("xxzygbwf2@outlook.com", "wla252805"),
("upgojnsutn50@outlook.com", "jzt419910"),
("mjlyoyuuj76@outlook.com", "cnr574335"),
("ahwulogalc5@outlook.com", "fld702419"),
("ekehjvms65@outlook.com", "zrh047757"),
("lqinbwnvsb55@outlook.com", "avl398837"),
("yamihxuqoi138@outlook.com", "yzu888405"),
("uqeracr556@outlook.com", "xnl186426"),
("hfiuqgpvug9@outlook.com", "nnr379725"),
("obzsfyp145@outlook.com", "jzx640696"),
("kbdtxdyb006@outlook.com", "bvj398275"),
("bcgwomf7@outlook.com", "zet065643"),
("abbpnkdm88@outlook.com", "szp150102"),
("fvthklw331@outlook.com", "hes926642"),
("uyxcamxd8@outlook.com", "rch293284")
                      

            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)