class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [





# ("mvharbw423@outlook.com", "ef0gbBIz0wq"),
# ("sxviwfp025@outlook.com", "uOdjdIADZi"),
# ("mqyexluohv4512@outlook.com", "Qtq3CwO8Fz4Y1"),
# ("oenzgcqgqq971@outlook.com", "nynrHsz793G"),
# ("rzggzuaku675@outlook.com", "t3nUYWADe"),
# ("riilxyhof344@outlook.com", "Ro72CXvIHajON"),

("pfeojzwf385@outlook.com", "rIlS5DRglWV"),
("aklgfdkg0574@outlook.com", "82o6iepZA7"),
("bzvmmrjyrd192@outlook.com", "jpFiI5xGZmUl1"),
("fpqzrgxpkr949@outlook.com", "etC3OkWG9zneg"),
("ebnmdvahoi7663@outlook.com", "v4FX3TfHQ"),
("hkyxavx776@outlook.com", "QobTPXNPOrhb7"),
# ("gfizcxpjx7487@outlook.com", "0YS3M229E"),
# ("tlwdhxn740@outlook.com", "1HFqlhFNXDtP7"),
# ("mqatnlkp193@outlook.com", "o5D73T6xTPZQ"),
# ("jsgjcuqdmo9081@outlook.com", "IYhMBr4xZ2"),
# ("xbotfqjez7282@outlook.com", "EC4v68uLHtd"),
# ("tmbfcvjiwe0108@outlook.com", "Xmr7qhmJO"),
# ("wlxtgnyiv1881@outlook.com", "ZWCCfo3OH5H"),
# ("akxnegrwm280@outlook.com", "eYTvo44SD"),
# ("ussqwujw8735@outlook.com", "WxdChKF4Ee"),
# ("yrhbccl751@outlook.com", "6clJ0ArFm"),
# ("isjceaybqy7816@outlook.com", "uviWkkHEHu9"),
# ("ktmseeva4689@outlook.com", "ssil7xZgw0"),
# ("klruqnc058@outlook.com", "1BMV5bTpqGEcj"),
# ("daskgzs3158@outlook.com", "sZncmHjFqsq")


            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)