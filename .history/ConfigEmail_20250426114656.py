class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
            
            ("rvengopad1115@outlook.com", "KabgAnoYd", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C547_BAY.0.U.-CjniNLyATAMWAQ2hZ!a85D7a74ihmlvK21h8sECJFMCa5sCK2j2lssEOr5lku*g6D8VWbCVHWR2eBKaFab0or7xE8!P1VW!XsW6bSZwOqOLexlJompu7iaQJzUlv9PE!M9XGdZtq2iVGIi*UlSM43xNAnBVORMdq9wmAFBQ95AjUnWvdWsd2bVqOELN3YL93Avp95foQfjgbh!2a4S!ZUq8416q80mw4hqCuFsBqKr1UbQBYpsipEjUgDIcPWHr42laihoTZ*tQIyKewNEehmMaEjiYJXwaUv*X8C8KI16GQXSVj*f9AfT6LwYYgN4TUvWuFhQFeG0FoX4kiB9O1TFvko8t2NhXpZfQRi9v2Z0j9eJpQ9fkbsqxG35m1vdaejKgh!abxAoeCXbantiddASs$")
            ,("xawvahjtw1974@outlook.com", "niqK7kgn1", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C503_BAY.0.U.-CtQ6*MNv4Cti49xIBfLthAVkreDtWiBqoX1Ua86Oony5nqQY43i6N9JdKMx5ciHLH3HWXI7!vzh5d6BD8meu2Y1COaRrCNN1a690d6RqnoAiNQohq2qIdaa4H4m8ceteve48woKEAzLDMPvbyR7nlHKA3j8kPKWS6ji6HA8ZlZrteEabSzfdQo3DaF4BL!IgE44WQvc70Qpp2jqqCkUdrlQ*wfupYLocjfAKzcnjc*e8JBJa60kAML3qiMbN97SREaCrVfMBmXL5VyKWkAmzttm*FaD4Mm38JX1P5MSCJsa1wXSoXMf*ldNNApmwMdBtYcqRHxYwjr*brAJpRk9UlazBTCBFW!LWSw02odr73!WjjFG09rbUKi8qy5BXXSRa1ueQlrfFILya7IL4DpZtnPM$")
            ,("sogazzuxn1294@outlook.com", "9u7E08E3O3NyM", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C527_BAY.0.U.-CoA9G40gx!d2WWb9A0xj1QaFkgVa!IMrk5vxTcY8xwRdtUrd2qMzRBwQef8L2!9na5GWG6IFNhbcVTDtM!vw9kUU8Uh*QscDHTkxuAh605O*OkFLX460Ra2Prg!5DoLwmxqtL72Ey7UFeH5D0ZqsXXUnrJR7z9RQBwlf2vzOKZk1vXgjtl7j6pG6RuosLc0MBKOCSlSAW9Cp!KhNkwIbKIa6tJgxsoY3m3tGLqbb1qO83b5jguOFjesal5qW3sZlZSTwfor11dMiUWjNUts2QyC*cynk*j7NIU6OhfAW1ZSl9SWiQlMxWUT9UK8POyifvF56sDevt2Lo!RA0Na0voW9dqfqhKfXIaxv9VrmaFiZ54IYTk7VjW2URL8qWNCxryUhbou9!2jqCq0v0vae3inE$")
            ,("royqzxu615@outlook.com", "xEEB4C4IJGl", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C551_BAY.0.U.-Cjp*4zeN!A1K3nabl1jmRmqhWS3LezNZMfZwX!IDuuKNFb6btDBeGrrKmHvZOXk8veHAsGPgre9sFOayf8wBP7pQ!iyHoDzs8o7zlhKCjBE4ZYfKYB8*H6foPdAUIXG9!8xWTs3aERkpaxPsmGodTVqM8I1RCqY9sbMoUvuTbYatxgRBzil88!J1KRkSTdS7OpCOTPSD4Qc13hcEO89CkBYmoaqBLjt3Y*VMkK!JkgSxLntGypa30eqNwtJDC21duHVIy7BuHjAeCz5WJHd8zluMAoLjMokuJY3X6A48K6KJzSfMn*Bok1!hM4uS7ovDO*eVJIPi93iAzfeqo*sutIgJunmjpg9D6HKnb6vFYekVS!axqHPgT5*maiDPyWIBziGLiuhf9OMEn1kVys4TOCo$")
            ,("occcacu9241@outlook.com", "fYsnuDTJby5", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C551_BAY.0.U.-CpGr1XwGE1oH*BUHH4Cr7IxFoyzakMpMBZUffudz261HqJoBGBkcDuvWfISXu1!G2XfPNYdiXhp!ihKCkBFVcIcl8gdf53D4hEuzmjoJCO38LWLN!lJ68umc1GsDBTDVmo!CpWpX6HPzg9kCIrbiQnCgfbTJR!kw8tXnZkapdr8JcF!XQFfp7Ph1*uQfL6ShxcB*S3!mgJ49NOZWkD*K7HXvaPzdzRfr2JI*m26DOfBZc7Y9v!PDqSGDMiH!KUvg5hnQslkw6RE44gzqS!b0!rz5W6z!rYLOMmRNzWToKENlJB318250jioLPWP3eN6ES360xR4sCkirJ!XZe1b9x7eqFSg4kQ0CZ7jNMcrp89IwqL0QGbbVW31u93ry!IaTJl*PY5PvkW8QOlSq8NDBJo8$")
            ,("uenjabcz2014@outlook.com", "lFsKitWLg7hLz", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C511_BAY.0.U.-Cg3xqzDQKE7M1f!nRzrL0kW3hy7VG7ciSbkE6BoDJIJMtuDobAJxIKhxlemrhDb6bstus4FUjT00DwVhDmGNxmbLPZoFwW2Jks7WkWSCRkBUR*qurqaLaavNTQ9Q2MyNBERapWZnJq7yY8azVOw58CCYGDiwcMFkI2I0jQSHI2zyDB8R3HNDrwuJnKZ8nSpuq4nhMPQqJcXOZOCddmvQNzna!C6dVpWw1*iQ06mur2c9yRbjGtYkYwEhqFFYb29iXm3iuU1i83VaulBL3m*R!CkWDgXRKB*ryxkyOw!Hb5h1dizmvy!W3TkYe1iko!MDCKzyNzypVvVD*covjADKzIwirDYyPsVsvRUWZxL5ugB1!6g1EIfuApoaO6byF01dwe7qP8pPmO8zT3k8E8wgwOg$")
            ,("djzhyog2440@outlook.com", "D27T6y0t67", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C534_BAY.0.U.-CrNs7fpSC*kSEVQxuc8OFv6ofqe6ASoqpYWa5YAuwUzWV!F03ngJ7ezedAWw3Z92JLTSxNqks63k642PhTKn8*EO*e2FP*PsG*4ttU7ijJ!YiDla2e4N46l*7eVavGPv3wnEYKtTydlbDFhS2AREckLANrLPnyfWuEtneZVA8aWO41qCl3lrkGIHxk000aWa6LQuOlWLTfVQKsOXgmBwMpiuFidm*cU5Py7OJtclhRJZC9b!*Qv7AyUDnTpl0WR8r95tNLGp3S0BZFozaErsMETFTdMQRXW8L5nLSnnhlEZG2THlZQ6rGAcYcAtYkb7XZy4XwjMs*Z*S9XmyLCmj6rfQ4ebECYolo76bT38qja91q76fxJcbdzzN1TS*qE5wWeAEwOVa2yx1IHDtRI95xe8$")
            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)