class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [
   
("DonnaBurgess1986014@outlook.com", "Donna361070"),
("MichaelCordovaMC1975@outlook.com", "Michael431253"),
("VickieJohnson198904@outlook.com", "Vickie633553"),
("CarlosLove19791113@outlook.com", "Carlos590184"),
("AdrianaCollins1988116@outlook.com", "Adriana231791"),
("KathrynAustinKA1940@outlook.com", "Kathryn458607"),
("LaurenBrennanLB1953@outlook.com", "Lauren831416"),
("ChloeCruz2005812@outlook.com", "Chloe135441"),
("LoriOrtiz199461@outlook.com", "Lori824440"),
("StevenSmithSS2013@outlook.com", "Steven493594"),
("SabrinaPollardSP1999@outlook.com", "Sabrina744279"),
("VictoriaEspinozaVE1996@outlook.com", "Victoria337593"),
("JamieGriffith196060@outlook.com", "Jamie488677"),
("JamesHughes198364@outlook.com", "James539605"),
("RebeccaSantiago1973122@outlook.com", "Rebecca694431"),
("DebraHeathDH2018@outlook.com", "Debra721738"),
("MichaelEllisME2019@outlook.com", "Michael144277"),
("RichardFord1987211@outlook.com", "Richard602244"),
("JeremySmith1962819@outlook.com", "Jeremy905633"),
("EmilyHill1991925@outlook.com", "Emily794424"),
("BillyFritzBF1998@outlook.com", "Billy142754"),
("ChristopherPrice1978613@outlook.com", "Christopher948242"),
("MatthewBird1973414@outlook.com", "Matthew701365"),
("NicholasBradleyNB2010@outlook.com", "Nicholas905922"),
("CatherineMurphyCM2007@outlook.com", "Catherine618418"),
("SusanStein198433@outlook.com", "Susan858297"),
("MelissaGonzalesMG1955@outlook.com", "Melissa861831"),
("DouglasRogers1963712@outlook.com", "Douglas277480"),
("JoshuaWilliams19671112@outlook.com", "Joshua177175"),
("PeterPatton1996611@outlook.com", "Peter497803"),
("ThomasWilson2007425@outlook.com", "Thomas479895"),
("CarrieLopezCL2013@outlook.com", "Carrie708989"),
("DanielFigueroa1995816@outlook.com", "Daniel596509"),
("TroyWheeler2010521@outlook.com", "Troy605856"),
("EdwardPeterson1985119@outlook.com", "Edward937973"),
("TaraBaker1989615@outlook.com", "Tara550036"),
("RobertYoderRY1988@outlook.com", "Robert286736"),
("NancyWelch2010018@outlook.com", "Nancy854263"),
("MarkHolmes198868@outlook.com", "Mark904130"),
("AaronMccarthy1973620@outlook.com", "Aaron636590")
            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)