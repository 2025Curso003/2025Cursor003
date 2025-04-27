class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
            
            
            ("ormqljd961@outlook.com", "TAhgHuFkPLJkk", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C505_BAY.0.U.-CiWxFqmphBNO5aeWF8O*YtATp1h7dyk6LencgiaWcw2iCi8Tx4xwd93dSGVZfXOIN9t*hELDLZsfpEqthe0s*ZM63lSxbqv4CJ*SxJBUDWzwZPq8QavaPrX1TZCwKVPpW8ktkssq8!EG7wBzp!fcl33O1DS*RToGGL2bROnH7beB*Wbg1RXWTgDZMKxPyfj0*OySIBiuBGM3GPMFzI9vgr9c*gqx7ci7CZ*CifsA9Oy0byff5ieRhd*r8reJhH2LW3xXC5kvgnIq*YUs1mRcDbkMHG1mKPIzjRH6h3fvf93GzPcDqVn5RzquGQUpY8rtrCdNHJiJA*ZNV26oJXG*HKaYqe93XTkrbWnHPOB9pVI67FefU5iZS8uvS5uw4o7iPrH!FwMjg0k2YVfwkogZ1Pg$")
            ,("krhrhyiapf9737@outlook.com", "gPh9Q0LqBWN6", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C538_BAY.0.U.-CqsRIYNxCzMiowwLRY3nRKxDcyaZOKL9FQ!zHlhf53af1F4wgvfFZ*ndQ0tMiDgPkD*!qdmLvQB9Psj3GXUOyuKEfUVBv*zLl0bweb9hOHNWiMXlMK*YE*HLB6x2ExExBBMJnlF1QMxwrziKLEkC2RjePAZiyEYw4OtcZQfomUqTknM7MgMVYIHh9h5f*U7dY45JQUx2Cj3xZf2euXyGK3JNzYDswZ1CJAYcElbxPlSrRz8JipxddfHs0LbxGG0CW4Uty5N9NtFhUHXCggokzG2ERSnPu3F6JhH9!53hbb3FQ3W1hIFZKZKHRVCDZK4k*Qx6m1eWis!qsrfW8zBAXlMUyRTKniZVnsJ!tkpKVakW4SYTHtQYmyDUGHdOeUObvajUbbN2JcPPM42bZvt9Zlg$")
            ,("ywfblqgzx669@outlook.com", "sPcKW65o3ykps", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C501_BAY.0.U.-CkSGMlCiEKZEuidczU2mdyO96!X7kIuOr3AeD5HDEIPtz*2SDNJZcQ7FnOsI7Rz*DUMY2En20JmfSudUiMRMZMv5s!jpRu5DaBtSKvQSHeR7vrbuUZ7EwqrKPu01WJgea9tqorVHs7A30Hf4jwQ9YGetElkk4geGy7oZkQASaG3lPuBQ*mR0qI9EFjFjwHO2CAGURShCUUWdEMoHnTtxTP3gaxiIPYNJaWFE8KRgMusRaFVH1Go5dpecg0KG*rpqtDHJ!4aWnWoeBNhia6UUWm1Wb1i3e5XBhibpPFyv!K*8twZViKFSgKBL2Hb8r25kXFrlLSdBF86fyVMlXaKaQOftobtoa*2y0ipgELNLqjRdjfveitQ*ZEEiI2FPQAjuX7TmW9ZUvsab0O!2bH96pio$")
            ,("mupkulbs1317@outlook.com", "Lk0gPLOqF79JU", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C532_BAY.0.U.-Cj6Lrs0DmMaIyHAh3IYpE2uGl2LBTb3O29K2zDvhjX8Iod4Zt8xQbg2SNclARozF9eDyJuKcw!4YYk4Nj5UD7wVIz7M9xRsdaQaXD8ybTHYIzh0nWC99nccnCnV!KQlztpWO1Jr42vhopPptpBCbhJv6XVBTHRkkL2ajdvADWLd98sfIFyshWsGhkARzXcXjBdVNHPW2ZZqR0!hmbR15MoJD6uH!GkOB92Z4bfkoF8lRHaQOL2I6fX9oIFcyvhjk!zBalcgxzXY8nhDsmMx0beL0ku!DOUz31eOPOfybJ*x!fXXl6z9ZdTbOfPO8fswwptCFhDW7GEPOWIWEYOEWbSJshlOAct1C!S*GkMsYn6VUlZnPAx7I1tIBiXZmPndDcHSvdfJbCBOKX9r2MWrxCAU$")
            ,("gvwppvha9155@outlook.com", "ronGnrhSHXAT", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C541_BAY.0.U.-Ctr6QMH5lHE4wH*NnsxhG4DpQZqK!lMyxxRITkBZzqbJCzOCfmCx01RLlfqKKnQHiY*U*nk1*43vHTVm1*SvSdGMRsZSfxog2cu1nlRWu3f6fmrprqjlkyYum8nLzwybTbXrPGG4HTOw6szokUXEUCLBC9CdciNrXTjsIlOKMwmMAA1UeptsYZrA!3vwGFxOm*KoEgAD9!Anbc!kGoprPrX5CbEahOkYk9Va39r5edpitIZEg2Iq34XX2y6vdcbb9VDe2aCjoUfbijWTXTnD0CWrL1TZ1rwuqJHLcxEBOePhFG0B8oHu9FOpnkAyFS6HBPhg1!BLkZTzrlmeCnJqFIkRfTtCqZPbMqVf*RqhyGAWyg!x0s6v3!pxX3Ifj!XJt3hgGoDYYwgGMo2gi6jnZi0$")
            ,("ysrnaufp9510@outlook.com", "ILmfuScNVSdbx", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C514_BAY.0.U.-CgFuGD8pvozv5TN05EHQ72Jo5gkwK59WtvgC!9NpdlahpLRKQ*YPJMjogqFLB*0bZ8KBPTBqoFaA9E0Dffn2gipsD7PkAJVD4omsGukB3018FjfiyA*YoiqEz59v*ythGnip0KNfdoT8!tVnX2X1nTSDiLwJZIGWAqr12bQpT5kVMdil7Ndppo4ytBLibm2VWJ1YVCoIozq3KeYpTUKSqRJoNZ*pnJSaSDyzpufEsiKH38Zs5xzhDQymbsXpItpOaKaZgxHjFjlqT79TKq0Rt2ThxtO1vicZlr2*M096x8wm49NtKtaF58gYhWDk56YZSqMZyZhLuD!xPkQ1RusVc1nI07nulfv9sSJMKYvULXznVysX1Qbjn*CaCjjond5Qv9y19D1UO1qXx0Aq2NEIJ*E$")




            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)