class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [



("alornuchevet@hotmail.com", "e9Cv6U80"),
("koonsbulaja@hotmail.com", "y1Rr2Z66"),
("vsacapra@hotmail.com", "nuaNO884"),
("vovkojucja@hotmail.com", "4OhTEN29"),
("aniiecialin@hotmail.com", "1ASNvC15")

# ("ajrgrmd8@outlook.com", "xdq230648"), 
# ("fbtju8@outlook.com", "izd119482"), 
# ("yhdvlmk71@outlook.com", "uxn933896"), 
# ("lmixzsauw4@outlook.com", "jkz980996"), 
# ("ozqjkei3@outlook.com", "ubr163089"), 
# ("evladcrcm74@outlook.com", "naa105968"), 
# ("aivfscakh426@outlook.com", "omj538342"), 
# ("cjmvxqh36@outlook.com", "vfr561220"), 
# ("jfurjnb76@outlook.com", "kgp118001"),
#  ("uimxnajwl12@outlook.com", "boz544735")

            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)