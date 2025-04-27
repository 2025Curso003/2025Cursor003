class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

               
                

("dlvqh77@outlook.com", "pdk562361"),  
("mdwkfzf7@outlook.com", "mol227598"),  
("ntrruqppp21@outlook.com", "ena061280"),  
("jitndczov798@outlook.com", "rsz231231"),  
("bgkivqork2@outlook.com", "zmm654942"),  
("baydvp7@outlook.com", "mdx239763"),  
("lmpicjgi4@outlook.com", "oxe250006"),  
("jndtxfacra600@outlook.com", "dio875308"),  
("hyspncr710@outlook.com", "osy205286"),  
("qeqgihqsy7@outlook.com", "pjk336884")

              

            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)