class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [




    # ("ntgxodmgs8484@outlook.com", "JMLQbk7ID0hm"),
    ("iprzxima558@outlook.com", "xYkiFslXypCA"),
    ("jpgkbuj0562@outlook.com", "zDTJwJqKKBFVM"),
    ("ekziobpw8106@outlook.com", "UfwbyqB25"),
    ("agkbffd300@outlook.com", "tISw9FYkIoRM"),
    ("ysxyfmgrnj561@outlook.com", "1CH3XpISW"),
    ("pjprnhnan3011@outlook.com", "ZGhEqcgTUqy5Q"),
    ("blradyk437@outlook.com", "xkk7eKcN4"),
    ("rifytosan314@outlook.com", "l5JQrktPsVO"),
    ("vlkxasg902@outlook.com", "jhagfG88zKtc"),
    ("igzrjrmce090@outlook.com", "7UxIt9XJb"),
    ("ejeacyyrfg067@outlook.com", "HB8DWZ8th"),
    ("ltkrqysd014@outlook.com", "SWSktpe43"),
    ("fxmncvk2323@outlook.com", "8gT2pbeCioC4"),

    ("uvdkbax4336@outlook.com", "hwKkSeWI7j495"),
    ("rzwkfgxspf2844@outlook.com", "W6E2ZhZ8XAc"),
    ("ehcjoky0353@outlook.com", "h7vbMxb9W"),
    ("mjrwpyt059@outlook.com", "vqw3aEAyQl"),
    ("tmyzbhy060@outlook.com", "WC6Z5SUiaSY"),
    ("daqyyup849@outlook.com", "udku7QtKNPUMW"),
    ("qjstyimij173@outlook.com", "p3P7Dh4fx"),
    ("cmndlnea1927@outlook.com", "FKXz30gMnr6"),
    ("iqahkmqev910@outlook.com", "znaNTzvy803v6"),
    ("wcuwecmjtg882@outlook.com", "OXoKsZJLYMP"),
    ("hwcayjt8110@outlook.com", "U6JqvuyjKRbs"),
    ("zpfddlneaj9198@outlook.com", "QICNLw9g81Di"),
    ("vrtuxqm8358@outlook.com", "ZU0X6xujUf8QG"),
    ("uzfufcqfaq1320@outlook.com", "i0lEFWCEiUW"),
    ("mfxijhadma585@outlook.com", "ihHZ81jX2"),
    ("ukvhnxxreg802@outlook.com", "8SdIcSHzdEXsi"),
    ("kqcizrjoeq0639@outlook.com", "YOpD5XRx9sZb")


            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)