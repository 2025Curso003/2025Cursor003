class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
            


    


            ("haarepitekkc@outlook.com", "zkBPUaZA", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C535_BAY.0.U.-Ciox8wXXh8MV7bpBokJ!cdzxfzCEiE6L6f6hEYRGsX63Czdy98W4xDAXH*kkMyk8*Cy!p7jxILsTgE*JbFe!UwhQ56fluPND9ccT3!CnbKqylvJTErFoy9Ezh!JeFSnaW2G*4Fj9yG28ycoaT!Y9Skdy1PgQFeDccBMcVPqvtWIKKnPhuNUP24z2NqUrrujVTGxU48KkmL94e5oQUXKh*!mcdFylgbNewrvNpd4NcekWoIIoVkKbES*CEK8VsRPJNtiHOfKxPnt2oCpxR6igTJiB3nGTnWzjHxRBZ994biW7i5XsODWMgLAqSP3QxlUFq0sDdD3fHv!!y1Eym36*m4CUBRiZIGv76uxJ6ZPJuUEHMod0cLk6Fi7NcCgAvoU*3h3!3yflSzc2I*0eljjF9nA$"),
            
            ("symonesakivs@outlook.com", "ArG8oGJu", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C520_BAY.0.U.-CrLAcHgLZQz9tNrv9LrzJ0GBkY4AQwtvcF3jboPMmMnsgH!zt1oQy9IzXgz7eAeV2kD5Td1HcFSiALBn2JbLaQxP1xFfIjuGG5HBnaSFv*w79hsJqg6SOdIIkLRn72bewB639LMyYURJ3HVmrLoAAkdl6cRSF7anOgd9SGZDgUZbvzNfcne!cA1Hg9O12DSwOnplBiuAugnjNcCxAUGveKaF7VY!Ljz!4A5TD*iof*clHmujpRS9PQ83p*oLi7Livlq2lHioJmpbH84*PuTbUnwURTZd2TNDLhjqyc0hU7NaXmVfObCaM0CgK8TBcnXYAP*GKnwj585zmjXBtRAeXJpQTDanJDEq!WSk6db5ofUCwn14c2ZRkHf*bIJ57!Jkfxjn1w4W6hyDyDI7IAcFl3ql6HZL4QIGkrZzRGXDFFnz"),
            
            ("casadkoene2u@outlook.com", "ASM7KQZ8", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C560_BAY.0.U.-CqlJnkF9MnT5AfDwlzoTQShYFZLRWjZoFJ*dAMmZUKapPtS!5AQcJQVNd1yrjFZPPgVf933ofDa17uRu8GiHtf5VVnfu0UhrX8nh9CUPxvayKtYsV*0QCZxhQohAJpryn9BANXxweJiF90yDplQa6xGa4ierkbEjlaxANTKFE5siSYg1rNaar4UPww63j1fApbPaU0yPMvKcyuSBE8JbXMn0A8SUkHoswtAGU1ocoVSogjDUnBF43XKLGuVLX!bTTFrrFxkNlg6VY1ONmBeW9IufVNXcljmfSp1*u3gzUtAaD31kYHn4BwcDCO140mTfFrJqUl*h6WRGve6WZQz!l*6BExsBwK9aIrGnUl55!YKtQxKgXfjS6ePqLC5ZFmWrE3tI9xs9GltGK39ys5ZTX6o$")

            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)