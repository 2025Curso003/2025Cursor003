class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
                        
            ("ogyxgod3212@outlook.com", "cPAHRKrWx2IVi", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C510_BAY.0.U.-CgBCfzuD!SV2kAtDjpRdeWkntv!pcaQjiiYJzxXFkDc8z47kT6y!B9rwtdfZGPoe4vYlW58IASeqUpGQF3EV8p!p60R*Y2e9RlKzvDo6Q5X4W06nzM2McREpoS1nWKPZv7HmM6!lPt8R4nEOiwuKsi4h753FN7*MGDq!bmVLTg1kIBfpHSA6VMcUwPfNDK9V8zQKjvuBa3FnqdyCtqASf2AnyeAihAn6sFSsxydKWwPzPIT!Pp56T0FBEW7i!if*m8tM4!haJAlVvGqNwO2AQlqJvo*sqZdw8hVx6ORntgshBaKMnd8rk7!IFtOKir4HVjcq3Jw3Jy8YRuzYJrUf2RSKICXVjRHFYSRNeOaio!9qW2yaqU2JgEmKtu04auE4ccWDws!29a6P0zOXHqSGZhY$")
            ,("rpzjmrj348@outlook.com", "gS1uT6WyuhqM", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C511_BAY.0.U.-ClfhMPd6suHCQp6**6aCKXuEbfeyT6zOozsGDwNj2y0LPAfrjOSWWw7NB9c1bMsR8TLEMTHDr4Zhvk*3nt1tM2wOexoIN!Spqkv8w*FpmtJMsI4l*7vaoocuusWlFt9flNlxnP85rV9Pw7wQLPpzsMH79!ztFjT1gCGJ*jn4VsKYMaZovgyLj6umMigWLOUt1SKD0wnFIS1BYYAgTIVieryITDB7ZvKqbkdvqecq2jStXsG9qfl!4k7EUVoy8NE0jXk*idhNBug*olU7VOvXPenFB*3CuJTRZmVNIoC0tKUrrNQDZXgk*GlJ4ERcK6pLk9yxoWM37*o!Y0K0L*f1KCJAKfr5brUTxMIxsOX9BPQPTJsqTyaD3wtFlXSt2nLYuo7DxpbdHzX3cSQQBB8uMPQ$")
            ,("luysfkal5292@outlook.com", "C3vGibnuwmC", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C534_BAY.0.U.-CmEaHhxCUIHBPU04mccSH01Fvi9aT6!0w7yCkTMufLxvKIvzvOEdviJfW7GSjz3k5nsY*uqn8*vIKhY1r8zVHweut9ZAkIYRHxCYwVzA2Mg5a7QWAObCCtUjIshtZC2ca3Ez2NAy0VZbzv9z5Zcl2a9GHgGTnZ0Dz938pjdyuHK2DReDLStXvlxSKdkvM02gxsk7cBXWMPKJi0mOwd1NIAp11R5o717LnWJpBnwOT1VJK*XJx6yjbKEzjJIr7VeRkW0!EfPwYgRF5m704NA0jBs5ln6ny*sUr9TKWAxqxZSZT!Ar10R8XCchhISZFGSILlyH*SuQ1GR0HDWUuvxK5l1U*BsDcMWaSy214VSir748q2Y52Mp!bbl0!dpqSLheqLRWx39!6iMEakTPm2waOAw$")
            ,("chdngshl7189@outlook.com", "vkg5mFbXGRg", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C537_BAY.0.U.-Cs!kCS33spj0MirfZy64bcZ5yKLB8LFhrT3Grs1IDu1A*fi6tO2CTWwxxlbUEKxiXRqAIWmSn8*qK!fjMnF3zp0pDDWjdUal3Y!fzP92v79oEwHD*3r718zM!tzcY5ShSeg*z2bWGPDJyNVRpm4*mVuDjzy*5MeGijSdRVrvQ0*bHu!tArwCyptYsOSWPXDk32BgqQReWrmpF0nvqBJFfHGeM7AZ0ORuk2ds4wDPrEb!4kNE63yPgKKkikXKahKvDH2476RAOgGBSzAt*m!8SHnU74oS90ZMD02DMD!fB6b5I*Ipay5DxqYSJVpZ9MlFw!Fw5RoVqRDN6*5V7adcfQhkPu!**c0xMH3bu8x4YW1jc17xiaeNwrbz2An!umWTujyjO6it9Ma3bp6AgxPrsqQ$")
            ,("gowslxtbve1301@outlook.com", "hQvZYVwmoyGFX", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C504_BAY.0.U.-CpDeCVp8cxt4rCjHUAYO5OA*HiTwcr9rBHTvYqZC0cK2O8iudtEzyQB02CmeYniQeEP7j5W!r93F7CBxAuJ!YuZQIwesLVy61nKnJfejxN7gpFCRDLDrZbSGbe7Guosid2lE*P8EWULzwdahcTv9E!iywTOZnmRnCRFjmFMqU5UEoK3CPneCqbWXQN9GNiW92P68ORKKcfFAmYfpymmTN8wiH22cnuIuhr99DIMpR*6gnRccSvrXDMoosio5jx5SSmZq9dxuGAM6i3D4FcgsVP*y*GBxvqnSdrZB1zyluhaxvtvx*eno3ehT4aBcKCmRSP7lwBFBweJTP9bcvBQwwJeL5VBOBHdfUHL69YUSe5tac7*nitLOpd*wtvq1Idfy6kvIzilqU8F0zEUGLWVtXRU$")
            ,("gsclyizb5701@outlook.com", "0BWE5vB9L4A", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C523_BAY.0.U.-CstX71Ffw4uLB6VI2OKhiJwNE44BjtypN9VFBA2b28iWXy7oKIJJzzsuc8hl3fk4uCg2rwYorRqd*WIm!qggM1yn66E3DqmCXr!DtnIrmREvwPuHH6Gkc9!O*3AD5uptQUNPz4HVJY*7D1nNh!9YLGhUb!rjnBNAedchEt3kGVh609nG*c3zxOysu*A8pYyiiRsR1YNtPQ80APzDrDwTzVdMCuxGk8R7lp9NifiIcmEs6Ln6pk9TbbgUudFZOgc9zXml5yZritc3brWTA*IeEWIilCpkwdSXA1auxxRr4yyEpgpd7bTJci*S2D4wyss7eClphC3FbmLXnBnaBK6hs!Dq43odAZA*XIs4BP!3IkhmX98GCupVMtNTlZJF4IMG98nGM7aHb1n0a*JN8q4TsXA$")
            ,("mhzoxiwfmu437@outlook.com", "paEQAo2xsF", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C514_BAY.0.U.-CoLYwKX!69OB0*t!m*QXZ6Ro0kPmRP1KPLFlIrkz*LZcN3yULL9koxVZ7iIqFLCx0*NHc1zlYprNZrz9JVcBcPS5LgXTaJn!JZw7nr1zrWtxJJESK4Nx!HLDylMHM2blPkNeOWO!Kl!CVXPc2mgc0v*K2S1G5KqPCiScFoZg5aZCoIl97Uhhtpj*cB9nDfeJXZliy2amjZly*Cpha2CHs47pWsv29AdQMeILPzaLbg!6RPQJ5eKo1nxKSM2KeFJ0Sx*Wj*K8KcfT36oN9IDHqyazlVLLpuTRusGxTnRzsYHieLavA!vOpPvwSTGZIRPe8RMGUfuhWOpPW8RXefwAsxalE*Lk6ZjrsP1vn!RTMVlnguH16vb88bKHCmj6y!CH!Msu9WBnM2a6ghVpYTc5QkE$")
            ,("mifnpxnmv7138@outlook.com", "kRKGAaabNCB", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C505_BAY.0.U.-CjWKhLvfL7DU78MMrv*MI9H3RgmWIsSe9lMSV7*7t4ptby!Qqzq9smsUm2AgrKXoTNuY81tZPTNipTHZadVfPBNNiDrcmIKIVGTtkI6GygAiIDXQ7BE*KusiMTIy44Y428QfOQicSyp7ZZhwiWu4SarxY5E1DpyVzmrxg3RD8dx0Myrhd3cleReHyAgMnoJ4nj318QKHQA1nGgamBd5WLr5LyqTSVOvTttjTXXhIIIpDwJnF4HtsM*OqWqaZIGWmc3JMDdWbYUgNTe4wZoFyEu4GixC5sNJNr2*Xl0*49ftQ5LqsLNss9JMM5xcRiHEiOyULuXTUYmQuMD3Aqps4S8e8FOSoj20j8cjjVH!nm9E0QRsZJCW9czymHcvLrf9j*CtyTYalEz0UqdJTk3!K3Ec$")
            ,("ttzrcrbn5508@outlook.com", "brXd7E1HoTS2", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C523_BAY.0.U.-Cru2mXRDk7ODbvd9oJ*!ZTDDm9LuLTSVENtR0A3BtMQOUL*0DP6qALFPlHCeXFIuJkfVLszRcIlFnk2XdDl2YW1fsxyhSw0y8Staqpt*PjIb*K3zVtir351uxxmBjB14bYaIPL89oke!K1rkf*EB8iD1G7t6Iy5LhL7PWhQU5TWryXVujXX1uxsruP5tdm!!m3R*KqSF7YalVf4hm8siZM6zJC!cCLQCBUVODBb!9NiQbApqojY4kC8tyViWerT4HKqcqxdQUOb4JGbDLPT05vvrRHX67x5XCse4U5PEAr9JkIIwtqMaRBfuABJMuE*yRQ*Nmh4nQpZalp4fyAvNJKGBcYzIO303ZC!THpdQySdxXNaja5!AUqe2bNGpqIXfuXUvMLDccs9A1ympWuc9wpQ$")
            ,("qayaauxfm212@outlook.com", "K9G1AgGNoICam", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C531_BAY.0.U.-Chk5vRuKTMj6OHsz2XB5d6teeH4nD7cljxcqdnG2!zYVWLqRh51GYYMxAlk1TDXs4rAsL0Y4XB4PrNbPa4lTLtPlbWlkxTcvbsljogbEiPTOL6dK8PhNuRVH9mr7*fIW4tzRXgCXjcH3dZ7gVG7yVkMdoRr7o8*Qr9DAJFdGa4qecH8Sz2bvJ72Eu2ciDuJo4IPfzqWFBlOrWKp4ZAmLT7pyGWaRxXPfND6YzjT9fLlbXCz4FEuk0IjghshFI1juE10wmBimvT0jiYK*R2*wtgavklqAjFdJcnf07g!Jdipvz!On1OUtcPZWILRaxAg2g0Ll6UL5KGul*A*nl3vAkV3auLHNghG2i6HXZgFXGIFyOtTwlv5Vkf87crCcPZg9ghfMyUnqE27PQJEibNADnyk$")
            
           
       
            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)