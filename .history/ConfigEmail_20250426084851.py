class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
            
           
            ("eppigtareksc@outlook.com", "JXh1yPts", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C533_BAY.0.U.-CnuLWWxTAyrLm37wCenjWnS00Oiv97nLwU9vL4Bz!ELwGLM63DK47cRAsOLq8UTLh*YdikJ0ulLNHNdIE1Sr5XTAM9F4i9tbDbN6jpPXji2idgW21V3QNZ9ChpDevV3sod9wJV*IoC2v9j6jFH6YWzzWdc8bLkhnQ7Hlaceb!U2nPgiXCqPwIatV4HOk4hurdffvBKlk6Hyw0L7s9r1Jgko7xPexvIAt3RHfEKuYCq*duD9VNleNsKQm*aKQXY5IdXqgTj5chDMUHn3eG4P7n1cMt*uaRUyUbFuUUBvsUfZsiVa8SCDE4h4tnD5DLLC93uzEgAxwripONax2nVo0IVNTol4iAvj*dByylPVe*oyGZC2EpQQyg!JXZhAzHE1HZOIVc!CCV4!owtkRohatBS6x5QjuAm*15AfiL1litE2H")
            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)