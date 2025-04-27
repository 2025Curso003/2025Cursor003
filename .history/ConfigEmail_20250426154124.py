class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
            
            


            ("caseycrickh2@outlook.com", "EGNzSeZy", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C514_BAY.0.U.-CuslM3RQ2tmTXDU7tRWIKMU59NJax9PmILlXH!GIWaCkq6ZE1JUDxjdf1MqI6Zx*66f6aKGLmFHhgKaehCcwnO*sUwH2MpwCM1VKDQkte1dC2APln5rbR62Ixh31FY2E6Dgf7N8C6AnHouARh7yQIWcn6SgdxDEZDouahoi8CB*V44G1sQPGPjpLxJLalqsMwGquoKi71!7!ZDe92lrEGEiRj7Lp1dPYt7Gn7hdjVCCkE5yoLUd*zdpf9TmBoeijbSgIYrpBt3fbtAgkrIRpgJZjw8LJIlvxtDNpR!dXMkewId!NraujykKa5XDKTuLw*wHSJVUikrdqfaYODO4VmJcjHvvlYkhLZd!ko9d1!INDmvrdF9E2F5NKIgNORgkCM0V1tc5S8mJ4!T!dp1xHqsc$")


            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)