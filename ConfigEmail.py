class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [
            
            ("casadkoene2u@outlook.com", "ASM7KQZ8", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C560_BAY.0.U.-CqlJnkF9MnT5AfDwlzoTQShYFZLRWjZoFJ*dAMmZUKapPtS!5AQcJQVNd1yrjFZPPgVf933ofDa17uRu8GiHtf5VVnfu0UhrX8nh9CUPxvayKtYsV*0QCZxhQohAJpryn9BANXxweJiF90yDplQa6xGa4ierkbEjlaxANTKFE5siSYg1rNaar4UPww63j1fApbPaU0yPMvKcyuSBE8JbXMn0A8SUkHoswtAGU1ocoVSogjDUnBF43XKLGuVLX!bTTFrrFxkNlg6VY1ONmBeW9IufVNXcljmfSp1*u3gzUtAaD31kYHn4BwcDCO140mTfFrJqUl*h6WRGve6WZQz!l*6BExsBwK9aIrGnUl55!YKtQxKgXfjS6ePqLC5ZFmWrE3tI9xs9GltGK39ys5ZTX6o$")

            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)