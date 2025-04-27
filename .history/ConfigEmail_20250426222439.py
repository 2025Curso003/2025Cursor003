class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
            


    
            ("dorchstinnt9@outlook.com", "fmbvfMbe", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C550_BAY.0.U.-CgDR7EZNYag4lExoEtb2RXA*4WaoW*v8YpQRboRRn4XXtVz3s6B1lm0*gABCer6iZzIlhQ!j1y5R9Wrw3Wh9GPT1DPXur7VsFNjYBS1WEY7*9vCGNv7mQQeP0U52AOFaN5GCi9iFOOjKLzXCwZd9h0dWYv5B9q0Vx0ScC5wYyfl84aKEausGV4zTKCR0RkaBPX30funO3JpWgEFUTWVirURiqKVacGBxKFMVaalDdmlhNN36qkrxaejwCiRudm5SL3WIczIZmgFxcEg4H6s!p*KgGRx4yMO69L0zklPH7rJ*gfvicF!JID!v3Vgfh1JSJBADVE3r7222rnrSrjNSBGqYljib!WcPuGBpM9MORTGwzda3m1kowVv*MZDr9C!g81QcIwGyxTQGQ2BTAqkkQoY$"),

            ("loseralgusw5@outlook.com", "vjLlQYVY", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C508_BAY.0.U.-CkWEky7YengYeFyIekTRGBQKQqgwtU0HeA5UdQ*vPBVU09x4r12RPz*kD6J2FZPJ64!IwQIyc!Zw8dr!jj!toCLaE3Ym6xJ6f!vBx0R7vMAYMjtYkDriZUzPxDsw6*AkuR13!bQ9298xKN0*sJpYBVLwziIbN9DR4sq7QWlXpsuA6d1miJbMrkYSRxIBk2826k9c6lDRE3iVI2iOb6tTZXmVccVkccqDLtpk7UeMle2jmVCyaPjiesu6Pl25PiNuBb!gLdAfx99YkciKo8zhLfrKdPavr8NcKdZh8EXz5lqIxfaT3Ox4g8QWRjLyZb2M2zsyuxBSYQ*WbYffkKk3hN!q0YKSgTBAcg7x6w6m45wtoOwHvywAtWjo!zedLIAaFa4kl2aGNU3pvaGkT!JGHvo$"),

            ("lipkasifres2@outlook.com", "aabTmT3C", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C517_BAY.0.U.-CjHKeTzBaBk5f64q8pHD*c6B5GCrBmC*XthArEX8s04dFysWR6Vk*QLDnU0WLFCKQl2vqACV26Qo2qpwk!AAKW3LgaCmeyveNCBtP0CjY7SLdOKpxtk2mp9CTAT*1emiCR94odNU15u2pzh8yybzczE8GrV!cR4m3v!r!UwEQQW4txtpcblBx9cyiXj3TQWgsZqu6vZKvewuO*TFOfp!wATvfpbKMRa7hkbIUvAbr1epBkZ36uVPv4KW4*mhZjC*TZxhorJRXTxseFuNx3PBklw7k2XiT4EFnillceCg7mSXc0CWqbBpxEhsylLjh5aOoWZWCwtactDWUyzNPkN3F7oxl1Vxa9TjZZ5ypW6FcgcNZH2!Qr*KjGygBCbGOlqiNXs7qHUOsyZoaDJJ2pla1DM2DuwmjvIkCpUoNh2JLjdz"),

            ("cerristaumvv@outlook.com", "zXgAy2UP", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C501_BAY.0.U.-CmkrKW*TFAs!p*OSXGUzfA51QLkpMCxw*h9lOolojzyKzauzlx9!FE!wkWTWaaG7gylM4y3saEME6qAI4dAGwb4rVPYL!B5i0WQ7Aho!hoofzxpiqBiFTUJ9V!B5RWSmlnwuHpPWUeIBZLf8H6cEbmxytShvEHv80myxx*UtMe8j5PTQeTUq9Hsg1D9bIKBH8Ax1We2Oi0O6R6lx5psKevX4Ezd*qmz4H10zfcsKaL58*ibruWR4Md58AZaRKi41DFnt09bEe9uhVjfZEPeZRAggYvYXozV51updSeMK92ieVSRoYCVe5LPz4srjn8Rht*LaWnf0J*KhBbc3Q4iTDpIodocXo7AQ*WlpCwFosPp2kd7n!PxasmSJxn1kQ89fOUVkVjiyUZKVxkkvxQtotiI$"),

            ("hansegulyaxw@outlook.com", "pernIBLG", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C508_BAY.0.U.-CuO0t6uW28c!fWkjmqtXxJEyqhbRPWdkenh6VXh7YTRsXx3OB0!4dVBV3abOmuO4mDezbjd0*pnlECUVrW6HcSNJ0YUOPp8xe51jx*etxoRvJTwsPatHAwU9Wc3g!T*azoqCZjImVBZupQJi613g6rGqxpAihfNFrcwfnDoZh6sZpfG5uLpM*3i0ag8hlYs8EsX!NTnk3!YllynLHKKzyPqO3p3zFX81y6tCMS!XlS5yhYc*DLTB5NArjsiPIXKOGqxh9yDgj8BBjTLlMRXWVFKe415sWHzT0Ic*aQ9MFxUIu*3vIX3sXIHMCLcY5AFSkrupWc*Nq1PUJt!fUxAv!4PbbXguBcRjU3YZ0NyBY6WjixpYvXgKeBmCb3sDWMBt3udC4WoeQy2J0GdEvnKAmFA$")

            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)