class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
                        
            ("mifnpxnmv7138@outlook.com", "kRKGAaabNCB", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C505_BAY.0.U.-CjWKhLvfL7DU78MMrv*MI9H3RgmWIsSe9lMSV7*7t4ptby!Qqzq9smsUm2AgrKXoTNuY81tZPTNipTHZadVfPBNNiDrcmIKIVGTtkI6GygAiIDXQ7BE*KusiMTIy44Y428QfOQicSyp7ZZhwiWu4SarxY5E1DpyVzmrxg3RD8dx0Myrhd3cleReHyAgMnoJ4nj318QKHQA1nGgamBd5WLr5LyqTSVOvTttjTXXhIIIpDwJnF4HtsM*OqWqaZIGWmc3JMDdWbYUgNTe4wZoFyEu4GixC5sNJNr2*Xl0*49ftQ5LqsLNss9JMM5xcRiHEiOyULuXTUYmQuMD3Aqps4S8e8FOSoj20j8cjjVH!nm9E0QRsZJCW9czymHcvLrf9j*CtyTYalEz0UqdJTk3!K3Ec$")
            ,("ttzrcrbn5508@outlook.com", "brXd7E1HoTS2", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C523_BAY.0.U.-Cru2mXRDk7ODbvd9oJ*!ZTDDm9LuLTSVENtR0A3BtMQOUL*0DP6qALFPlHCeXFIuJkfVLszRcIlFnk2XdDl2YW1fsxyhSw0y8Staqpt*PjIb*K3zVtir351uxxmBjB14bYaIPL89oke!K1rkf*EB8iD1G7t6Iy5LhL7PWhQU5TWryXVujXX1uxsruP5tdm!!m3R*KqSF7YalVf4hm8siZM6zJC!cCLQCBUVODBb!9NiQbApqojY4kC8tyViWerT4HKqcqxdQUOb4JGbDLPT05vvrRHX67x5XCse4U5PEAr9JkIIwtqMaRBfuABJMuE*yRQ*Nmh4nQpZalp4fyAvNJKGBcYzIO303ZC!THpdQySdxXNaja5!AUqe2bNGpqIXfuXUvMLDccs9A1ympWuc9wpQ$")
            ,("qayaauxfm212@outlook.com", "K9G1AgGNoICam", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C531_BAY.0.U.-Chk5vRuKTMj6OHsz2XB5d6teeH4nD7cljxcqdnG2!zYVWLqRh51GYYMxAlk1TDXs4rAsL0Y4XB4PrNbPa4lTLtPlbWlkxTcvbsljogbEiPTOL6dK8PhNuRVH9mr7*fIW4tzRXgCXjcH3dZ7gVG7yVkMdoRr7o8*Qr9DAJFdGa4qecH8Sz2bvJ72Eu2ciDuJo4IPfzqWFBlOrWKp4ZAmLT7pyGWaRxXPfND6YzjT9fLlbXCz4FEuk0IjghshFI1juE10wmBimvT0jiYK*R2*wtgavklqAjFdJcnf07g!Jdipvz!On1OUtcPZWILRaxAg2g0Ll6UL5KGul*A*nl3vAkV3auLHNghG2i6HXZgFXGIFyOtTwlv5Vkf87crCcPZg9ghfMyUnqE27PQJEibNADnyk$")
            
           
       
            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)