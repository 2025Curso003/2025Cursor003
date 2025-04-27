class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
            
            
            ("ysrnaufp9510@outlook.com", "ILmfuScNVSdbx", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C514_BAY.0.U.-CgFuGD8pvozv5TN05EHQ72Jo5gkwK59WtvgC!9NpdlahpLRKQ*YPJMjogqFLB*0bZ8KBPTBqoFaA9E0Dffn2gipsD7PkAJVD4omsGukB3018FjfiyA*YoiqEz59v*ythGnip0KNfdoT8!tVnX2X1nTSDiLwJZIGWAqr12bQpT5kVMdil7Ndppo4ytBLibm2VWJ1YVCoIozq3KeYpTUKSqRJoNZ*pnJSaSDyzpufEsiKH38Zs5xzhDQymbsXpItpOaKaZgxHjFjlqT79TKq0Rt2ThxtO1vicZlr2*M096x8wm49NtKtaF58gYhWDk56YZSqMZyZhLuD!xPkQ1RusVc1nI07nulfv9sSJMKYvULXznVysX1Qbjn*CaCjjond5Qv9y19D1UO1qXx0Aq2NEIJ*E$")




            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)