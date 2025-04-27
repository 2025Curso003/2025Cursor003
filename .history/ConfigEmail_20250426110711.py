class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
            ("qayaauxfm212@outlook.com", "K9G1AgGNoICam", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C531_BAY.0.U.-Chk5vRuKTMj6OHsz2XB5d6teeH4nD7cljxcqdnG2!zYVWLqRh51GYYMxAlk1TDXs4rAsL0Y4XB4PrNbPa4lTLtPlbWlkxTcvbsljogbEiPTOL6dK8PhNuRVH9mr7*fIW4tzRXgCXjcH3dZ7gVG7yVkMdoRr7o8*Qr9DAJFdGa4qecH8Sz2bvJ72Eu2ciDuJo4IPfzqWFBlOrWKp4ZAmLT7pyGWaRxXPfND6YzjT9fLlbXCz4FEuk0IjghshFI1juE10wmBimvT0jiYK*R2*wtgavklqAjFdJcnf07g!Jdipvz!On1OUtcPZWILRaxAg2g0Ll6UL5KGul*A*nl3vAkV3auLHNghG2i6HXZgFXGIFyOtTwlv5Vkf87crCcPZg9ghfMyUnqE27PQJEibNADnyk$")
            
            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)