class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
            


    

            ("hansegulyaxw@outlook.com", "pernIBLG", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C508_BAY.0.U.-CuO0t6uW28c!fWkjmqtXxJEyqhbRPWdkenh6VXh7YTRsXx3OB0!4dVBV3abOmuO4mDezbjd0*pnlECUVrW6HcSNJ0YUOPp8xe51jx*etxoRvJTwsPatHAwU9Wc3g!T*azoqCZjImVBZupQJi613g6rGqxpAihfNFrcwfnDoZh6sZpfG5uLpM*3i0ag8hlYs8EsX!NTnk3!YllynLHKKzyPqO3p3zFX81y6tCMS!XlS5yhYc*DLTB5NArjsiPIXKOGqxh9yDgj8BBjTLlMRXWVFKe415sWHzT0Ic*aQ9MFxUIu*3vIX3sXIHMCLcY5AFSkrupWc*Nq1PUJt!fUxAv!4PbbXguBcRjU3YZ0NyBY6WjixpYvXgKeBmCb3sDWMBt3udC4WoeQy2J0GdEvnKAmFA$")

            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)