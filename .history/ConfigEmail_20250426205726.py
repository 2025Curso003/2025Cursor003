class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
            


         
            ("epwznrkol727@outlook.com", "YSVfnFy5MJi", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C509_BAY.0.U.-CjWjNrs4WWWmNha*kRz*lTJwwhXdM2dEp8rn9mWgCkRVqCZFqSdvzuS*QCgUimQMsrCp6BbDTogCCKZ7i4t6JiDzZ!SfIPEkdGyXLPGT6xRDQHXq47fyZ9nL6!f6ysjYoPPagejOAW0n33UVfMpqwEnOYpjfRnQNcUpADWjXm47oJDd*Sir3aWkMvkEnc4BKZR!o28mMDdhads*7ixNbejEk6b2MwhSJ8kd8Qa03OjApasOG7WhLa!g*latxwNgTCaON53GtoaAFVyiW1!kB7lkX*d*EYcAjmym7tZQgmWr7I0kTYgzsZ60hx5ZnQa7Ibnqg3oPvm36hr979g6Fcvl6zFMODlhMBRa6R5tIdVg9mGtCdaKfNXkaV7W7Vux0RT6wZms8btqX4g5xiBWxzHIc$")


            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)