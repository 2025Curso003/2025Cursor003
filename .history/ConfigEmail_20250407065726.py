class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

# ("vaocnfl0@outlook.com", "ugh574844"),
# ("kvpucde8@outlook.com", "czf543817"),
# ("xxzygbwf2@outlook.com", "wla252805"),
# ("upgojnsutn50@outlook.com", "jzt419910"),
# ("mjlyoyuuj76@outlook.com", "cnr574335"),
# ("ahwulogalc5@outlook.com", "fld702419"),
# ("ekehjvms65@outlook.com", "zrh047757"),
# ("lqinbwnvsb55@outlook.com", "avl398837"),

# ("hpbihdkmu4@outlook.com", "owx855860"), 
# ("cydjewlkbr29@outlook.com", "bwm681746"),
#  ("ktckbmgjy3@outlook.com", "nee191171"), 
#  ("wgbbpgkqx3@outlook.com", "eit688535")



# ("fq28228425yuanzh2@163.com", "lzp1276"),
# ("to67295350luliao@163.com", "vh38910"),
# ("rwj87998429bijihe@163.com", "ut68345"),
# ("hlhg27639268yepao@163.com", "ysg4883"),
# ("ozw6127348shanyo@163.com", "yan51089"),
# ("xior13601156weiy0@163.com", "kqp2650"),
# ("pp3580665luxing84@163.com", "nb36596"),
# ("bujk3552346zhan@163.com", "mdy678574"),
# ("tm3321896weiyun@163.com", "oxa304110"),

("fnmtfweh00628@163.com", "wbjh856579"),
("e3339713poyou423@163.com", "tmg05795"),
("y48872621touliao@163.com", "rta13126"),
("luxi7405zhangde@163.com", "ed910956"),
("shi09feijiaobu@163.com", "twp322870"),
("o7027772yongwo5@163.com", "bcs631953"),
("tg40258753siqia@163.com", "yat841544"),
("u8733013qidaozhan@163.com", "nk74289"),
("lpsn2130993xianq@163.com", "zn554777"),
("r21473021yayili@163.com", "qtv32407"),
("y4976373ziyiyue@163.com", "qgl02554")

            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)