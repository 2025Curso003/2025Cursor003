class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
            
           
       
            ("jcpmzzjgw7469@outlook.com", "HIkw3HUxDq69n", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C522_BAY.0.U.-ChYnRFOs*8xOe2FkprtWJE9NDV!cLvop9uhjhLs2dmga6T3MstTwdUqMcD22X5lKPE0gnWQUF2ifgwOZtBaIP8siEgx2!ZhilRLH99qVFXRm2pUSg7L7PS2UKccLCH5zjPkOdYyZbIKU9GEQcxdSK9IshNEaM0B26KP*fE!*G4mV*y*ZIHcogVwEa!HQvASze6gNxIexf0B5UFc0X21*5SwsYUS3kOkS*w9Nc4t1gwNlA5m13R*eCmtGEBsYwgzBz4ddiTbSlxdKaZxqQxW5VCnpG1THDwn6U!o2Kndd3EIVKyepLLgZm6Lt!q79DirW0oq7lZJpWApOq*rz3hcJzqgX2BGvM8tcp0EueoNdj7jlVm36YUh3113vCKGBZwftG8y6!DTSVVsMyU5S0O0QgQE$")
            ,("jovnrpbdt164@outlook.com", "IUZUp3rD3l", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C535_BAY.0.U.-CuuUievEcXZQofbr13l7zKl5T8LXqUvh*ru2UuU40WqmpzfdVda2jXDF7UI94e9eduvzLBJ!ZP0IUWRUhIN1sfApR82UGd9i1AMaEs7e!A8ixKKWFMd0VzjL1K3fF9aZgNTX9fCBcydZty9kpwM9hsCSUnhXTS9C99N7nfJmHILecS9ugYmYWsD*jRgdrcHteEHfj7Iz3eBcu*ogRgWDUq!NPwZxpgeKmigXa!GQJ5a9x!M6GLhGTfH083UgodWE82BffBvTcp73migSJLpwRK7Qg!0RiBY1kRXWNt85Z5M!h23*kxzPftppdSz0p7pRDDDaRAUiR32*qByCpbeOx8cp44FmsqJxE2y1pNx3VeGl125zR7IXsrEaw75JtjBWFhDeqDzr6GG0Vd8burkci7s$")
            ,("msngzluu308@outlook.com", "KrgjR5t1gYp", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C512_BAY.0.U.-CrmzlbpqNyl07MdTBTXX2JRFUftWw14RxYnnnwV6Oiwag3Rgpw9SZjUuHxI7Y6kfRAIyGibACHEcWwdXNgM5ZCY5cVVX4C290N!YvK8D24PYO4hs9Un9JnpgvDJ5WGeeQgTyfDdFw!NM2MwFKc1J*wTlA85!!tHXHFnFOVGEhwhUGgyesZILvq54eL65dDeiB!2NuLguw1IFoAWGvXiuG2uDot!A9XrLZS!k9wna6*cDldrVEc5chLhQAQwUlxj6JSicf*4MiQfWjY!GYFBjo60AKaViU!bO*e*zdK1Nh7Q5n48*sH*dBVu*hGKZxNC3kMr0ivf*Qvd30Jr2Ah!3gbMIv6BuI7QwRawCxV9oQY9zm4UQdOFMjNzqDC9!EVGLEZGAGKwbqoGDiIU6uJN7egE$")
            ,("dukzqsvrwj5610@outlook.com", "hGITogiuFe", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C532_BAY.0.U.-CnD1CThXPF45kBvTkklQXqFmvZvzOhDSzuT9kISNhYejWRfo6!4L6xF2Y*DoFEubiEZ2dwYZ2oZfyU6KsdONpaVA8r6s27fRUvK8p61GHuV0gTIRP7PreUZTd!eb5XGXp0MuX7APQAObWLVJJFrzLurCnZ0n3cY8gIBK8f9h!*5FZSpj3BO4mGPojdOHtrnYtJ0I2fAzYN!CvmLXFLCiEzoQfkY7KDUT0fYqDT2AC2KyIqGQlgvtMhH*1EFE6KQbhHpN0qKHt651x3BPsrxo3wwmirLBs3GBa!XD*uMqDmf5sCcMsd62CAH!6to0qTLX1KYJ7Z3YJ3As4P4hel4gBy4o*60mJELxH6fnGPmmn5jgc0nIS80NJWcGlBmkBoIH5oiorgD9eDVKcS9saRPkntY$")
            ,("fxdryms9530@outlook.com", "8qdYTDKRWnO9", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C556_BAY.0.U.-CvdghwlmrrNT7iS1RHDbgfmEYO4TLOiPFdfzMGdfDh4I*I4bt5UuVcC4FYs7lHUry*HmKqzqsPbxlXOjn8lQAX2TDMmQ5thgMu8em770XFbcoPx7uf1k0NWyqpWwE5Nx6Izm*eyg4*ElQL7QOYFsOo3gjqIMeieasJUtwLwBOHNlQ!J7bvXM!MOMyoabw6WCYE1WEikAL4Xv7K34VQ!DfiDqRIbsmrkhgffuFu4UBVKCv0DZGTgho6!OeUhAd!RI4ytqx298qFhFeGrI02w46jP3h3pbsiwFbD*WwVv3chqg8X09v72uWraxX*cs4vIkHspxFZkitcNWaU!nSJMROM8Wzqk90nFLmusTUcO4bEf!K2GsUST0paJOpcL0wo3n1SmsdgZbQ3M4mXLqtiMK8EM$")
            ,("uwkyilixfq3206@outlook.com", "OjhlFHroZg1", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C555_BAY.0.U.-CpnhDlZxL2BOKO9OdkeohDuYXtBaZMi1JPQUgGCe8DvZy!6Jm2NlH8nk0Y9RlXQPUFGIrAiXdnqbk3wHG86nauwM8OZD2xXneYeg6biBhrO*ypGamiRomaam*vl1yFdFjAL7HY5mbzHzhOa!QHDJOBzAaxhZeVNDTrrtkepvrArL204YLa!uRmqQYPfQSo82YEko!daUfkFeLg7Y6Y3I*G7jQ2jEw*R1oJa96YfSXD1n*BJwDF0yUKgKdhBmA7oUopMYkdBcGyzU8MOLKo2CXeZ3FNsJIY3t*Me2lPV!oDyydOam98UtukxCiWzeaNtWidFmcydTleAOrfAokTzKwjXfoAMlq8EzAXcdCtNzh1bIf1LtBQqIXn8gW!12bkJJAV9vkjqBYWdwkyUAMiEbGj4$")
            ,("rzokfqggjd309@outlook.com", "kpetFRqohv", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C505_BAY.0.U.-Cv6ignNUA12xv4Y0Hmmilznjc1HwM7PNwiMhXyB6zc3jGS5r2Sfjw0LnZo7Ny8qrSFVuWCSq0x*QA8TKPQcds7cn4zltF86m2GJFNXlededFDPsat9*xlo6DMq1yqzaVMf0iWQyVMZVwLs29skHxeB8i2F8GhLaUIUjgmzvYL8K!J9fA5DCdkR1J9Rs1DJPrMCkPtXFwfon6l!6OsGbmG3Lfriacr7PShYiguIXoX2VRgp8SC!MBRC0V4QLd9DYIleRxT8wjBfi12BrL2xNrH!F2AbGVUCXMdtdv2**mU0Ct4HseAXYVvhdGm*eL30mNbg1b8KW1bkLRwzkFABki1e*Jy0*lJWy!ctr5Hu7Qe6qaa6fezN96BjAne5*LZaXiLi1*G3wldsb2SWwQM8Tn*ng$")
            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)