class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

("MezaRichard6461@outlook.com", "lnbthjq4624", "9e5f94bc-e8a4-4e73-b8be-63364c29d753", "M.C538_BL2.0.U.-Cii8bsrQSt0FU5ajkl*JH6sVtO5I1iiOt*y7u*MgXRMv1TE94!hCiz*e3JjlcngGx4YNmEgbztt4WSXAGwFC51Kw9klYPUJPwt2fUqJb*aBg16ZZVeRrvTPTJ8rLfV3TmHoAwWIKX!rch5H06BprSuSpUxU1ct*!OnakHs3lI4FxOago4tqArHB2yTD5LcwnTGavrUlumkx!qQuukxLBomCtSXXmHy*p8gzvoaNDUOjXhsvtqhIq5XhbpF1gCDvcoXp*BlUEC9SZIcuq3gLmsFICJbnLSLy7!x3Jdq9wX4lIPRxJYv!vqVe1AxNrF8tdSc0c6BOmN3juHcBGRLcZJb6OVvpswcAbge6Ny!pIASiZxpwbC2VZCY1UyqoHahhuzmfo8DqQbJgkr43!mbuU8wpdNUQ7Aa69ooOtxCNxXgNgKRRuijqRslcGmTv!rqzrrhb5TOa7FVGJcB7ZWe1yXLc$")
            
            
            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)