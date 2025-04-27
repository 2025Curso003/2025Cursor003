class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
            
            






            ("qvgxrgawz046@outlook.com", "rRIlwFj6supF", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C509_BAY.0.U.-ChBoqTdTP0o9b6ymvz45U*4BSBp82HD998EroZTmlK7Ln0Qt7FOkVGxWRhSiltsOV5TziohbP6GV2Dl32rKxRQ!BLFD0c34revTexCwHHw0GR5KgUgOld559VBXwlErIW!LAzoMQSduqGzMuWbA5ybYVQq4mh!Fv3q5fqN6m!!KIMxSd4vJZ*ZRkkk8pmDkAOnq498htJnSkJ4M*FefpHyd5qrocUu2Lz4I17gbR7mr533gwe6zLqr52!06T6uSttbXA1msAhjG2*TQeb3I7q8zvavtsfXe9FSE5abGkDWLES3QCD!!L8alg79lv1mcPZU5qdXetSmnlIIdkmMh7wmlqkftHp7!znNVr!U4ciuKDR1fYct9XqjM2ROxVI7Ck2CoFA83lm9S6!SrS!ndBajk$")

            ,("ormuygi8761@outlook.com", "QOxHhsi7IUkNL", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C518_BAY.0.U.-Cu28kDqXXw9UGgS!ZyPsmxytRqBwPKsdYxYFmHKivn0nsY6Hnyg3ZpHsmVjeSF6Tg2F9s80OKIqv4*5!nVvEPTIja78uMlNrtg050qMoYyzewQg620xhRHQsMwm3huskC5uVQUKExxBG6zO2!wfcHtVuaTWaswzXxk53pdXS4wFk0YV9iwmzFWmUdBC7*lFpjMldXUs*K01145CVLXe6bfoucNa4ZXvAEAGhm3Q4e39zMe1swtJK9ry4CwtXtAY3haaENatbr9XcH9jbp54AssoC6ioMcNcJFeCRQiAwphp63DpTZo!IdVsPEyQXFLsXGqt2M90X3ch7LJ!1VHXWmrPzn82xCxMVmf1JGIMl42D8mPs1b4jSch4Gi*RrPPXVJD2JmwkRVSXIXuZB8v*!ZUw$")

            ,("akqaraomrr156@outlook.com", "54t9x9KQhVi", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C519_BAY.0.U.-Ci9sBMR0BNRfEARwz4Qvj2z2uiGjrBhc8oWMmL3Jr8jo5S4wk!vqAEdQvSZsFUnBGaDI8urFfT!fvI2CJSzBvGMN4N3RXSBCPNtwLS5W3iVN9uhaBuavqTODUjx6l02oiNwqCdiHVj6a5nSj!asYur7UwZ0tkdOpTqEaOXQZJhvhA9k1*Gk1sQS8zFwWe06Rb!BxawkYHXKMwMIfgTeCh2jXfs*9Jfwb6ZPLhxXi4o3MQtvJG0ccFf2QMXWOeuGaQfTEqmPNBOYILBu0a7GGELz3bz2V8J1tVSp7u6zdB2wCVsZKqk82dMvpHNLMleD8HmuRJeea5cwHhSfGSHyIuux0lQuy60LGAwrIc1K6OeU9Urt1FC!6XyaIwXugiQZmRIMyXiFf74MS3OJDPFpa4Ac$")

            ,("dnbpxqki4949@outlook.com", "K4LeLr2kfKSb", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C544_BAY.0.U.-CqmzNqlcFwDsOxgdKU6tvJ7D244c3sehefAcA0CJOvsUvYIA6BjherC**bSn2fDjwu4WJ3Sx!XBeEgSwNaXBIii3sk5BNRr20a8fjl69Kc1Qxmsl6IwZ7zUlqTNUH6dEWmb0jE7xgnK9PRB7TB3G5nwSHUJeuGq5Pw7QOg1s4U74ynTW5z89GnmUXs9fm17eGem0psY6l!ZDZHcI*6E9cnxwheJ!9jQFp4khoC0nicIab9GQNgJzKIElAF0tto*r79FyN8R4zXMQTCELecdgab*UYjByfl7bKI5!oRtSMrjp8JhPRs*eF4JBSbVVFUfd1fi10Bpr8Cgp7yac72YB9MP8aH1BoGcJGOi0ox864ruHS6wCdL75Yh*GJB!eMGe2vyL0nInTQQB08szIjIkbE1Y$")

            ,("jnoycawg331@outlook.com", "RMpymBmky9qo", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C528_BAY.0.U.-ClD9Ct26XKQiRZh*b8bjRHYi7vPjwngb1ztYAcp5s44myBDyjjDjdJTNlRnyUWbpT1ySr6zjYF2hQOET3RShBjqNHgkfkPQyhH1oj0x1npSgGEKwaVb2A0mP!rQquu6mnpwx15ER2u2TfmE1c3RoqvUvtQnmcLWZIqPfPY4OlMAful1mRxiJQgd0rarpt7Ftl056XfZGaFDGNLxgtYENSHelIeCkCYYGq9ao4Z0YUbEynd54r7xO7CbtKnyvbGcPenfH3Zejb7Vo9J!qPrWMb2v0myFhhaoFeZyIISEI2w3BzUNeLucxVbJfAOMFFbujFZ4iaCT9Xr3rr26DSPLAdpmbqj8umv*Q34zO*m!afh0vRjHHtVsRHHdHR2DyP0FEJfzujezlLC*kz*g4M6Z!zMM$")

            ,("grdmpbsau525@outlook.com", "c0ea31XX5JVw", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C524_BAY.0.U.-CpNbVWftsvKS6TcljE7sp2maO8ShL*oYoEtgklCa0JVnMz5breKG95iv9bFbY0rxBb1n3G!fwiXsTQfIeeRiSFekJupUzEoGKRWsxnTv!CILuFIm4!ug2fWj9SMwW6Bq6tN8Ybb0DQnc8hTzQVTG5VASzUs!dFQmIzg9q2ABHyi4L0g2u2rS3vPyq7CbJt3XNYxCxaaoeF6exm7p8qSkA2mhBJZEQ586HIgWt8TEXy*8imvWQYqz7k*FRwnJ52H2xb7iED2YSyvBPkDS7WfVZUnb!XS0b!zD2rmQNi4ec5i82ExvUG5mu!6xmtbp1hZXqvBM6DME9jYYVSUUwbpDoqJEZQwkgSO0gn5okDffXBa68qtmb6AD*1p*ZCKOBt*o*h59apDgbEhKAYy*H1MPUw4$")

            ,("teauooibs2861@outlook.com", "jZVeONBtVB2Zy", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C506_BAY.0.U.-CqBmcERNJa0iZ*oOEVEkcO7rChc2bmpKEVu8OSj*morVl4SLMbCDntj0M4bmVM7FuIH5qH257LBCfbIBI0eTtmVNF0vMMDkVQe20eytXvp6h6EKJT6VBi1sK565!hvOBg6Ac!dgkm9pP!LsxsPxfNbE84Gvb*w*8iZYRfoGPw2iOP4Ag!h8zTcxqm!H7QIGLusXZ6OyOE*et8UsNHiwYQ9MlYokZkeVlYtpquBWs38n3OCcZbWxEop1zj4mpYR4rZjHVDOoQacXkwMVEF8eXw4La16cAb8UoZlSeY2J06oT7FjhDYoeoCI9NPMo4tC04Dhz!sYNFis0fDrLR!fbVaIPfcC8cTY8524kpOnIjT0DWNmkbAXBk93vAb3rXqCcGwqpb3NtIQXp*hjeGf5TA0Xg$")

            ,("tseqnrrcr1872@outlook.com", "jpfdJaSsrbsOp", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C535_BAY.0.U.-Cm067UR2puR6QblZwNRsoJwsaxcwugllgMunlyXVpaHS*0m4bKLcGKHFnyHEZrl7zY7UizeFGsrjvsOKH4qe!53HmrqULWQD16jrR99C1U3hxqfNBNCeApXERwHfpapln7x63CfOgFcU!QWZLUH4eHMv3lenv20Rd1!XykzKJqmd*VG*1N794TLM7gouRd1LrQfXkR083YS1Ulq4piiSer2P6djbA!wtqWVSb5SC0bvun!!bQV8QP7OUtnUJIS6UEUOp8ndEbH2tJZgFN4nJp!Qwbo9sZM*NE1PGAlhX8mX0WCQBCZ3mGZaU99zpYVHbaRCK*q5u0QpSYq*FNLvCGFWaCZp5vcwbRNPZffZfIfRMHXJMK!xAZ6w6ecjZOT5UMhwAJQ6W3HDQRK0w6QnzUPA$")

            ,("clhwrazitr0166@outlook.com", "14VvWZAR1wZQM", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C558_BAY.0.U.-CtzSUFHcjdVQAFmuAHQnG15H3JugDfGT5ofe*tXsXq4Ai0vGmGm0J!7a7ZPbO!5b1eUPNztuaTyS84c4MUrEXLLZzFjeBeCV6Cz1KC5ToN!XwcRWjQs8LTobDF0odzYspE9*i9ocOZkPH5F2g95RuTvVYgNUoaMFqM!fb*YII8Morw!nMJYJ0CKSjM7mzzkI8BxeA7*5tBDlGbElwSOy*RB2BFZrZMF5yoQPYQP0QIez22WOhDXWUqGDLDuCQYEMat7V0XQ1lLOGmEaIERVuSmhQhWhA!8gGQ5YHnW2TFVi0z5VMpyJoxNh33rmGX97dEHOaW4zCP1sNOLqzvAL8H5DphUlNw9OcMYHTYpgReL2abkuQgJKQneXoCITb9UCjjFzIXtTZgDR*fVFuGRAUXWM$")



            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)