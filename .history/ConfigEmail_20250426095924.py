class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
            
           
       
            ,("fxdryms9530@outlook.com", "8qdYTDKRWnO9", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C556_BAY.0.U.-CvdghwlmrrNT7iS1RHDbgfmEYO4TLOiPFdfzMGdfDh4I*I4bt5UuVcC4FYs7lHUry*HmKqzqsPbxlXOjn8lQAX2TDMmQ5thgMu8em770XFbcoPx7uf1k0NWyqpWwE5Nx6Izm*eyg4*ElQL7QOYFsOo3gjqIMeieasJUtwLwBOHNlQ!J7bvXM!MOMyoabw6WCYE1WEikAL4Xv7K34VQ!DfiDqRIbsmrkhgffuFu4UBVKCv0DZGTgho6!OeUhAd!RI4ytqx298qFhFeGrI02w46jP3h3pbsiwFbD*WwVv3chqg8X09v72uWraxX*cs4vIkHspxFZkitcNWaU!nSJMROM8Wzqk90nFLmusTUcO4bEf!K2GsUST0paJOpcL0wo3n1SmsdgZbQ3M4mXLqtiMK8EM$")
            ,("uwkyilixfq3206@outlook.com", "OjhlFHroZg1", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C555_BAY.0.U.-CpnhDlZxL2BOKO9OdkeohDuYXtBaZMi1JPQUgGCe8DvZy!6Jm2NlH8nk0Y9RlXQPUFGIrAiXdnqbk3wHG86nauwM8OZD2xXneYeg6biBhrO*ypGamiRomaam*vl1yFdFjAL7HY5mbzHzhOa!QHDJOBzAaxhZeVNDTrrtkepvrArL204YLa!uRmqQYPfQSo82YEko!daUfkFeLg7Y6Y3I*G7jQ2jEw*R1oJa96YfSXD1n*BJwDF0yUKgKdhBmA7oUopMYkdBcGyzU8MOLKo2CXeZ3FNsJIY3t*Me2lPV!oDyydOam98UtukxCiWzeaNtWidFmcydTleAOrfAokTzKwjXfoAMlq8EzAXcdCtNzh1bIf1LtBQqIXn8gW!12bkJJAV9vkjqBYWdwkyUAMiEbGj4$")
            ,("rzokfqggjd309@outlook.com", "kpetFRqohv", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C505_BAY.0.U.-Cv6ignNUA12xv4Y0Hmmilznjc1HwM7PNwiMhXyB6zc3jGS5r2Sfjw0LnZo7Ny8qrSFVuWCSq0x*QA8TKPQcds7cn4zltF86m2GJFNXlededFDPsat9*xlo6DMq1yqzaVMf0iWQyVMZVwLs29skHxeB8i2F8GhLaUIUjgmzvYL8K!J9fA5DCdkR1J9Rs1DJPrMCkPtXFwfon6l!6OsGbmG3Lfriacr7PShYiguIXoX2VRgp8SC!MBRC0V4QLd9DYIleRxT8wjBfi12BrL2xNrH!F2AbGVUCXMdtdv2**mU0Ct4HseAXYVvhdGm*eL30mNbg1b8KW1bkLRwzkFABki1e*Jy0*lJWy!ctr5Hu7Qe6qaa6fezN96BjAne5*LZaXiLi1*G3wldsb2SWwQM8Tn*ng$")
            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)