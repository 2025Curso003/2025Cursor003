class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

               
                
                ("ScottMccarthy199824@outlook.com", "Scott889988"),
                ("MonicaJohnston200437@outlook.com", "Monica698488"),
                ("AlecPetty2004101@outlook.com", "Alec371493"),
                ("JanetWashingtonJW1970@outlook.com", "Janet773730"),
                ("KimMaloneKM1993@outlook.com", "Kim455406"),
                ("GregoryNelson2007813@outlook.com", "Gregory866908"),
                ("SeanSmith196783@outlook.com", "Sean933514"),
                ("AnthonySalazar1995111@outl1ook.com", "Anthony667123"),
                ("AprilThompsonAT2015@outlook.com", "April534574"),
                ("AngelaMoore1977213@outlook.com", "Angela389152"),
                ("EmilyKim1992011@outlook.com", "Emily920474"),
                ("CaitlinRobinson201035@outlook.com", "Caitlin794931"),
                ("CatherineSchneider1998015@outlook.com", "Catherine538881"),
                ("StephenBurke1962115@outlook.com", "Stephen282150"),
                ("ThomasLopez2005719@outlook.com", "Thomas262189"),
                ("AdrianGutierrez1995117@outlook.com", "Adrian175292"),
                ("DanaWhiteDW1973@outlook.com", "Dana738763"),
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