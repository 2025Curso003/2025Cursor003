class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [


   

("LaurieKrause19891210@outlook.com", "Laurie203934"),
("BrendanFarmer1994624@outlook.com", "Brendan843603"),
("AmberCook19931017@outlook.com", "Amber306586"),
("WhitneyWang1984913@outlook.com", "Whitney900951"),
("NatashaHenderson2009622@outlook.com", "Natasha414110"),
("JohnBenson2000421@outlook.com", "John244222"),
("AlyssaPerry19631224@outlook.com", "Alyssa573528"),
("ReneeSimon2010822@outlook.com", "Renee128461"),
("EricaNorris1998627@outlook.com", "Erica505992"),
("TimothyChen198362@outlook.com", "Timothy970147"),
("NatalieBrooksNB1956@outlook.com", "Natalie245453"),
("NoahSmith2009114@outlook.com", "Noah225099"),
("RobertWadeRW1978@outlook.com", "Robert685942"),

           
                
            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)