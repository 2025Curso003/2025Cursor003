class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

               
                
               
                ("PattyLopez19801021@outlook.com", "Patty579601"),
                ("AnthonyKingAK1960@outlook.com", "Anthony312912"),
                ("JessicaChangJC2009@outlook.com", "Jessica955862"),
                ("AlexanderLambAL1943@outlook.com", "Alexander520274"),
                ("WilliamLewisWL1987@outlook.com", "William618999"),
                ("ChristinaSmith2007814@outlook.com", "Christina731355"),
                ("DannyJenkinsDJ1971@outlook.com", "Danny527450"),
                ("AlexisAustin197422@outlook.com", "Alexis876791"),
                ("DanielChristian1990011@outlook.com", "Daniel145262"),
                ("TammyRay198193@outlook.com", "Tammy183040"),
                ("AngelWilsonAW1941@outlook.com", "Angel823123"),
              

                
            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)