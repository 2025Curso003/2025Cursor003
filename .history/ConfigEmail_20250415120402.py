class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

# ("CatlinHarveyfpz70100n@7to.us", "Truong3979"),
# ("PauleBarrettcii21967b@7to.us", "Truong3979"),
# ("MollVelaett38751n@7to.us", "Truong3979"),
# ("BereniceCrosbyxwa25186g@7to.us", "Truong3979"),
# ("JulietaBatsonftk76699r@7to.us", "Truong3979"),



# ("ClairFrosteoz13494r@7to.us", "Truong3979"),
# ("GladysMuellercdn70419n@7to.us", "Truong3979"),
# ("SibelTylerhlv85403z@7to.us", "Truong3979"),
# ("TiphanieKellytkc50053r@7to.us", "Truong3979"),
# ("EllynnBannisterypb74853m@7to.us", "Truong3979"),
# ("NatalyaPrincefay51772l@7to.us", "Truong3979"),
# ("LoreneWoodwtb97076o@7to.us", "Truong3979"),
# ("ErichaWilliamssnd33724o@7to.us", "Truong3979"),
# ("MollieFordnpa91079s@7to.us", "Truong3979"),
# ("zmfmhmsnhfmfmj@gmail.com", "ffgghjkl"),

# ("duqgzdrel57@outlook.com", "lxpcu19819"),
# ("hevkbcges83@outlook.com", "bbjq210070"),



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

# ("fnmtfweh00628@163.com", "wbjh856579"),
# ("e3339713poyou423@163.com", "tmg05795"),
# ("y48872621touliao@163.com", "rta13126"),
# ("luxi7405zhangde@163.com", "ed910956"),
# ("shi09feijiaobu@163.com", "twp322870"),
# ("o7027772yongwo5@163.com", "bcs631953"),
# ("tg40258753siqia@163.com", "yat841544"),
# ("u8733013qidaozhan@163.com", "nk74289"),
# ("lpsn2130993xianq@163.com", "zn554777"),
# ("r21473021yayili@163.com", "qtv32407"),
# ("y4976373ziyiyue@163.com", "qgl02554")

("ajrgrmd8@outlook.com", "xdq230648"), 
("fbtju8@outlook.com", "izd119482"), 
("yhdvlmk71@outlook.com", "uxn933896"), 
("lmixzsauw4@outlook.com", "jkz980996"), 
("ozqjkei3@outlook.com", "ubr163089"), 
("evladcrcm74@outlook.com", "naa105968"), 
("aivfscakh426@outlook.com", "omj538342"), 
("cjmvxqh36@outlook.com", "vfr561220"), 
("jfurjnb76@outlook.com", "kgp118001"),
 ("uimxnajwl12@outlook.com", "boz544735")

            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)