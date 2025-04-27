class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
            
            



            ("fsrpyash340@outlook.com", "7pMCv2wkcdP", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C529_BAY.0.U.-ClkIKON2ShOETrCbs*79Kb*7tHafSF9bEwGCUkQfpVOz01BtqEj6e9s*Icw3QHtZ86*wW6b8bV*Q0jeiG2QbjnvGRPVrcqJXhcpJXdlJKlBUPrYaYTkJ5!zX10iO8RvE!MQ9nUaV3bMkDHeKm!Jn5sr5FisTMFlOBLdJGbmf4MylstevD0ZRNL5F*l6lmShVwy6*VJXqjHlmPNRJL1*vAJfklEjh7TNON88EKgdJQnZF9ZFsO1gV*99NOOdhVViKJDU60dVVR6fO6IQX7mPXY50Yk1!PrmUEIXqZ1HrO2wQI!bNEuw3GAKJrq8izAKkJhCs2CDJGPsXr*p9KK1dc9kjAiP5es4WIDIMyuRFnYlTeMN4E8nEapoFvp*A6Mjv8UgO8!uB1A2*xC2YiMZ5Lwls$")

            ,("dhwcqpkq1393@outlook.com", "NpD5sLyWVV", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C544_BAY.0.U.-CrgP9Gl0RTsGFQK1di9M9lwfogWnMhHwFviQ1kke!AgUv81uxYFbINB0oQUDu31AIDbdel1tMzvylTnm8bdmVtzygP7UQUp5qOkccWOOmjulQUPzQCEImefJ3MGHSJ7HO!VJdElLA2OTmTstlvFhv1JteMb2JHJQSByJnyLzHn6f42Nk0p2ZM4AcbEtGKNvgoZCQ7w*S!jk4Lr1rCXKBRwiVbRO*xBzTNn8ThMfK4yAMQLSs9Y11Mi0XxVKCnma0uOKctxi5t!P*5idchSFkCI9*MAAXr9pBc0YHTp050P6svFenkefOMjRaUChaRgaVzKEDWb89ZS*p4EYlyZHCIUFaQLL2xHA*QUmGRPTiLOdwf6Q8fW0wI!uS0ks7tCYIn4RQY75Cok0Ifmd2I*7tza8$")

            ,("tggnruqib5785@outlook.com", "wKDLJ9ALE", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C554_BAY.0.U.-CoIxNdqGUJSXqo4agmSvjnYLhMcbN5J4pIW4x9JlXqWTv9W1z0jCc*SXLd8MANm4K*oyMDxxbV8Juokv*wPaa2IsdJKmmrqIrpvQuW1BO!g7gGUycEgmjyMfJf7cnkFM3aWL96kiymQEJOnuJyVq7Qv5yc!dBbF35tzm0Xbq4qrOQCAV5HHaAfJaEFp3WEZkz!vb5bBroXB*GfA9YxvTMiMMcTv6eJzNleBBXv90iioBphVnfttULos3W6m1cmIA1FFsegkMK7W2yYwdcUKlConzs7PPZlF7WBp4mmn8FkyI93n4VyRPH974aS1i8V6LJ*tHjgVZSDuU0zHGbJK6WoXZPMuGsfe5U6FALCugw7Ze0g6kSMHDSCNBuHNUMeHNhaXGpU64B1848YDwCzZaazU$")

            ,("rolcxvyrqw255@outlook.com", "abRkmJ0YwweVZ", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C550_BAY.0.U.-Cpdy1YlMtq5Zf18Yvw5h7fdWfvVAYvwgjUGOOPr!COT5wJZrVnnZg2aeUJMr8MMTkthLcP7cEhYMdD3YuROIURf0u*BRKZ32Ls6c!E0Dl3vAb!w!DMANwHrnEHSI5ONbXD4fIbmkPev5yx6OWbjEqpPGhTL5AzgNbg9X3XmVyoReOvWDmJdP9gidPMgoRsT*tvitDwEPfTMH!Je4Gq3swpRXKceLd6sJx9DADHOY!XLPTO1HXFDK6HrJLiPh48wDGe78l17DjU5jP7AcoYc3IAHVOqzp7Jx2lq*Dt2KU850babX3QN264Qu36v3BeekaNuxeNUcZ2qtIXaFg0m7u9syAXeK*WbUBcnYqp9ug4YYszr0m0KVjJ6uCRhEeWmGJTvwRDENdKtYASuUIRoEYbQ8$")

            ,("uoguxwxfc3453@outlook.com", "MuXbpt3NT", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C561_BAY.0.U.-ChTxBVqXC!VMsIQBqksG*L4o!M90CYjMNbyhTXEJ3gHHuk6cZF7jBKGOMEBEhxAdKjyb0sZFtWpmu61zxw11rL6H8ZAv7sXzY16uAfapDlGsBRfWrvBf8w0iWwQZ4A!Gr0LVbKYg0ueV*ZyoaC4wAoWxmzR6RqyzWyf66AwgmXzS9Kt85xZFZbcy1DWKu0enYTITxPbYx*PrrMeutcduw0T!OQjAXPYRXycFPYSz1xvI2vEPxjZ4gLun64E6ROjikhvRfbG4hFTL6Q4jLJnOAwD5l0v1Xa49aS!ouJXYa63GKR2VOEGXuilG!j!*x99FBqao8OgR*u6NQsaTgvQy5iLVJC50CerHlYaFDlIwt2NoZAtyluD6kBN6MGTP*TErxIZfLAvzqJ2kRrUh5ZQPGdE$")

            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)