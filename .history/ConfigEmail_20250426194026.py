class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
            
            







            ("tseqnrrcr1872@outlook.com", "jpfdJaSsrbsOp", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C535_BAY.0.U.-Cm067UR2puR6QblZwNRsoJwsaxcwugllgMunlyXVpaHS*0m4bKLcGKHFnyHEZrl7zY7UizeFGsrjvsOKH4qe!53HmrqULWQD16jrR99C1U3hxqfNBNCeApXERwHfpapln7x63CfOgFcU!QWZLUH4eHMv3lenv20Rd1!XykzKJqmd*VG*1N794TLM7gouRd1LrQfXkR083YS1Ulq4piiSer2P6djbA!wtqWVSb5SC0bvun!!bQV8QP7OUtnUJIS6UEUOp8ndEbH2tJZgFN4nJp!Qwbo9sZM*NE1PGAlhX8mX0WCQBCZ3mGZaU99zpYVHbaRCK*q5u0QpSYq*FNLvCGFWaCZp5vcwbRNPZffZfIfRMHXJMK!xAZ6w6ecjZOT5UMhwAJQ6W3HDQRK0w6QnzUPA$")

            ,("clhwrazitr0166@outlook.com", "14VvWZAR1wZQM", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C558_BAY.0.U.-CtzSUFHcjdVQAFmuAHQnG15H3JugDfGT5ofe*tXsXq4Ai0vGmGm0J!7a7ZPbO!5b1eUPNztuaTyS84c4MUrEXLLZzFjeBeCV6Cz1KC5ToN!XwcRWjQs8LTobDF0odzYspE9*i9ocOZkPH5F2g95RuTvVYgNUoaMFqM!fb*YII8Morw!nMJYJ0CKSjM7mzzkI8BxeA7*5tBDlGbElwSOy*RB2BFZrZMF5yoQPYQP0QIez22WOhDXWUqGDLDuCQYEMat7V0XQ1lLOGmEaIERVuSmhQhWhA!8gGQ5YHnW2TFVi0z5VMpyJoxNh33rmGX97dEHOaW4zCP1sNOLqzvAL8H5DphUlNw9OcMYHTYpgReL2abkuQgJKQneXoCITb9UCjjFzIXtTZgDR*fVFuGRAUXWM$")



            ,("rtavtgy773@outlook.com", "YTjdHYkguhtY8", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C561_BAY.0.U.-CjfDmaPXWiQZKTodWqoI2a4xkbeC7U7Yq7ayI7GazlOiTnM0rnglZhdA4Ah2eUafLMMw9xXr65tythkX!kVjXknWhqGnVlB3PArfKcRwvbwoG912YXQ7XacqTY5L4Es9nzw!!VpV0xvPPimq9VNIOP3I7Oq3xEgZE7rjgI4MG46OEPwfw2EBSVdG1AEnw7ven1wBmVRaEpbNqvbAXWHRTVAla8wHEFSGHl2VHYJ31jZy9M1hMl4SDbfJBIXxHnezf3gF4On3F58QBlx6UTNS6XSvrc8JiUwTUwsZc4Bk7NSVOPltZBHX9IEX5oBYZWiFtaHbXdu1CfBLdnxSMbslHespw**Alp04nuWxDxDC5lixPEuaMZdy!v8!KQSKC1DlqWBsrFxwXuUjF1Bkty5*imQ$")

            ,("kevncla6361@outlook.com", "FzdlotR7MUF", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C534_BAY.0.U.-Cl*J*dNiRroi!VwGin4NE15e3Zx28miMCT3JyQr14nmPmofHrFLtQCNFQyJ9qvoZ8phvrflkr7Ejfp9tD9WkrKfX4SbS8WyuBF4njGYAUMFK0DdnwdI0jjOFMta8IVHhEvb0bMXQKsxvDecaJUWtNMNmextfaAgcP1z0qPuvr9yLKPSreNSqnIBuP9!G4hmvqx4dpoL8X9kme!kW1GkvmZhMqGwbyDQ!yKG49hRBXT5KjtvL2b853OzDijFMZxZC5X6OuFUogS0Sgymfnw0pANwzA!wYPMFEdbP*PjHVKCCMo5SzneKoRhy*LrG*zwwyDHh0BbnDs4AY8xyQsEoXSjHhToYXGVSO*lMVZ**qGtJjJuzIgCpm3pe58h1GEeivgAih1*376jEH7vdb8MLQ8iE$")

            ,("tporvzhsv2442@outlook.com", "cm8cW2QSFff", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C548_BAY.0.U.-Co9hDT1eIcT2zLE5F*qbJfns6T0a*QJ0bB35*8TswKBetoX4MvykHgMGa7aqHgkLcnXWeZHTOJAuWYrM4pqSFb0eeGnHbMBc3EsKJ7rb6z3CzyOcOue1fXntsL8gVB4Gq*e*QnkD0K6xvyqH9zKzDMqBVzbN82uGVmFi0hOyjM8JEY0ZGcBD6tT0ME9SSGkU6xmHwOTo7jaPIJv0M5BfCVWjjeveClDQo54HCVKbKZttwfkoFar0fJ*vDp1OE247lGuxvQPd*q16EWjLrcTPI6TI6tDp0gsbt3aQ1DU5OcTvGOqNbWnaPrPaW7sOpv*zQ1sSgu0yJxyFEIYSTWRnwGT17U5vrnLRIIFwDZnU1yKvMl7OTk60xbwb!DT5sbbkd9K9mcVP8YtkwX!ovkcJ!XA$")

            ,("iagyagdgz3647@outlook.com", "AUzvEjmPy", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C508_BAY.0.U.-CnIPE4rB9YUQqyuR5sdNTD8BZV6CAiSQ*JaRP!FXezTsKXhb5Hu1SoM5FsF22*nCcAAVDgTyaRhjcyS40Tpg!lMg*mvl*ud4CUwcdLZbb1WSQJu5f741db5MI1tEEkKjwOjwdVJBy!hchnRE88KILYYzRu9Bpsgulv*53OPTWHuTyZwEGv7h!Awyfe3X6i*zoCurleQ5p*!8anRpQireNlFGRJBhQ14wQsX1ATv8qS0k1HZF0BaLOcQ3xgq1SVY6bzqz2ZFUubPtzd4NcCfhqXzDEstvEjppaiaPYt*p5xuS88dYOjuYkAHkfkQoPOmLhF9HDw25qb8JvvA6VPN12z*irMUm4kVxeSUovsyKJ7yNTRX6FE4*R1YPCmA5XcNDcX8Zm7vRynnNeA3z1jq*2os$")

            ,("dnyjimrh583@outlook.com", "iunHMzwQq9C", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C544_BAY.0.U.-CrSnCXmMsm7uKLeRA1Vacn9p3tCrZwkEKcCns!SAdlCZH!cQVc708KG2LerA8YzNfCyWmiA!mHj5TSsmeqnnHEIpFZKj4YyxkcHB0zgIddqmLHlpSnt6Uq1Bn9xpCxZuqGR30nyPrlDedAgU9t94TK6CWNd*7uQQQgqAS8QLWiQ5Munsl9sFEvATUC*pyex*NCgbIXkSHYI!8MLpE0GcW2lt3Ejc4SpvOcBsiAchMHQc8usmk6Lw*8DhhMruS!hh*3Gxz0gPjdl5lxT6Z*tBjOlN15WkkBFz4wcwVzBJ7dUE9Gu4rTwgzMK17KP7pPnA0bhMhszvAhwzv6IJWBwixj*DTzgJNHkKbQDtEYZRjcA1sFsq8r5tif8WR7XG2a4pRVbibJHvrmkTSp6XkI*4wa0$")

            ,("kfcmuwxayf3357@outlook.com", "Q5DusUODffc", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C521_BAY.0.U.-CjVhiARV1Mg07Ccy484ZKySJxfYLLb7F5uzVb1VW35kR20c9TUeOAMCJ85GSEw4dBHS7DGNlT7SrjpOpF12*JbnjpMqsJfd0ZlLpuec7CASki4rNspLuYzNm8W9E!fGaOFFIjlKx*iC0FOE2S3ZdsCpHLEd9Q6zJVbNPZK0a5mKVTJu1iaLz6sGsdqoW5iZycXTekg1Rxk*xFpqCa9FGU81Ql1ToQxW26QS97C2styXsBAy*E8XJ4oOaE7hpfUNH03C7eENsrkm7FNp1PSGjl4m8ZX1hkOaMcX1tZJ5JCZg9HviMuzTAG*JqBxGhxnGjGx78tBQL1NDK1hm2C4sjlSVBTqoLA6c0jEe7ZV64hvOfT7cg0XQ*n2vv17ydH35nQX893Cl5lnw*iVjtk4I30To$")

            ,("nuxhduuoh461@outlook.com", "ZqGmGppOGZ", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C554_BAY.0.U.-CipqsFehVdIoxKVP!xRqLrpxpbAfpkgMhfTKrF5bhFf0dSGZIRBg*UbvMfb83LPBBmbhQSZCOU7IhHjJSeSlZAYXPAC5c!PWWcWtzKum5LDWK*xt0qJRAE1AvqP4BPxF50fCe!ML8*iU2RDftjxS4GT6QPjab0*9ooe*Jo775*9OouswKCoy!AHEKqjvghEiBym3BMSYN1FPuaiqzHo65WPYfM8hGllxjofA1JKVCoo24n7v3eRm22zNRgZoWoB4oHIQfG0hZ44jSQff9ZN2aoMc7vioKhlRx!gj8V3waMO8Qf9vAqq7VWqh81mwO*vuzwKLbE16215UMNnhvYOo1Ez7ebeogAEnkhQTlj4h!yzdX5Mz!I1rjiCXgWnD*o55yK*M6uu9BY*IDV3ztQj758A$")

            ,("amlhapu7902@outlook.com", "cRueJyDCv", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C526_BAY.0.U.-CqJUxbUjAwec!l738DjXHHKVrFbaTLNdsp*gILm8PgMV1o9xXu!gIeu6*W8WSvFx9L6JW2zRc7L1DFXj1U2udydRNU7Q7jRhdzIRBvaZSWref4IcsU8Beun4!n30pcrcx5wtKMGOFE!J7pg1DfP73XNPTNGCkZXGLd2Cp8zQLEEPBh0HUSlw7Enp!ZvakEhbQQFLTa9DmHv0GN2oKSPicAmqxZ!bPwNfLN1nRbxDKuVtulzQ3SAv4!dJMigjXnLOw5Wf486qRyMY0Qv8rzjqulXbVC5h7EhZL!lClnMtaMXO1sejChT!i9PySig!Wmt1a!WXvQTwI!AdYQMAOEJsE9D7OlM7KC4Zj4EzVt1sqlB3YvYwM0uuVeOM3tVIvmfchKP8jsJXFtHjiA8yc!5y1HI$")

            ,("dmirwqdd2078@outlook.com", "RG1UsGxGQQkL9", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C502_BAY.0.U.-CnKnApndUv5xdIyDjXpgTupQXYKzv129apjb8tSDOAQg4BGXeGgN8yK8pp!krGQNtW1FJBetn!3i1C4yrymoTQrfT05xvNSKyNP7UCs!4hkmwWvFmEcTR4Jnxk1Qyk5UH!Go2eVRFSl9ffC3yf1gXSSdGbI6LkKlFjHpuJ3MRuJGm5*9hIV*Rk!fypaym0wqnY4O9y0LGoEX2q2R3ZhCE9JDRmQAJHeGUwMnMIYnnnrWAs25zfkAzOb7Ro*dL!JngFQFkY00DMzube6ofUwLF56rDgf1Mn69e9oC8jeFWogQ7lihWGrx4XLLnantMooWmVExcKdcCpotqX3aHGdBzaD!An6J1oDc*umQtZyZ1s1wYSVx516UN6sxSEr26JQbikpR84KV6J7LY*Z92WXdftg$")

            ,("xqbiuld7881@outlook.com", "rU8En6n8Ni5a", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C560_BAY.0.U.-CgpphhqO1lX7mAIeubccKQe5LkkxA*GQUAGQ85GRla332NxaHhELku9lDHdQL3eFaE!07nPKP3dNvCePQnxBPvugy4PQJZQqm7OMan1YkPbJv7y1e4A7VN6*OlyROcPN3MZEPjXytYZieFM7OUyxo8*m0f844RhT5TTfymuslW8Iqzuz55zNbxFvjbnrHnD8xFD1YIz49FY8pbAwBaJg5wEXNV0GAi9VgjH!KQReX6M7D393y9kmvUpDpB7QcqzbGiVu!63OjtGkuM4RyQJvr9K7s7S6Qoy6b9ahUbH6364w!3!7M1rJLedhTQg5872Lpwy8wHA4O6h9valJrvkAH0p6rmPQ*k!AQ*NnRdmZACbjeDCuOT4rmu*t5SnuF23BOAYU3tK5Qr9xYjDzpbKvpIU$")


            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)