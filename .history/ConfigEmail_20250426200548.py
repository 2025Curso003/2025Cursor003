class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
            


            ,("dnyjimrh583@outlook.com", "iunHMzwQq9C", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C544_BAY.0.U.-CrSnCXmMsm7uKLeRA1Vacn9p3tCrZwkEKcCns!SAdlCZH!cQVc708KG2LerA8YzNfCyWmiA!mHj5TSsmeqnnHEIpFZKj4YyxkcHB0zgIddqmLHlpSnt6Uq1Bn9xpCxZuqGR30nyPrlDedAgU9t94TK6CWNd*7uQQQgqAS8QLWiQ5Munsl9sFEvATUC*pyex*NCgbIXkSHYI!8MLpE0GcW2lt3Ejc4SpvOcBsiAchMHQc8usmk6Lw*8DhhMruS!hh*3Gxz0gPjdl5lxT6Z*tBjOlN15WkkBFz4wcwVzBJ7dUE9Gu4rTwgzMK17KP7pPnA0bhMhszvAhwzv6IJWBwixj*DTzgJNHkKbQDtEYZRjcA1sFsq8r5tif8WR7XG2a4pRVbibJHvrmkTSp6XkI*4wa0$")

            ,("kfcmuwxayf3357@outlook.com", "Q5DusUODffc", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C521_BAY.0.U.-CjVhiARV1Mg07Ccy484ZKySJxfYLLb7F5uzVb1VW35kR20c9TUeOAMCJ85GSEw4dBHS7DGNlT7SrjpOpF12*JbnjpMqsJfd0ZlLpuec7CASki4rNspLuYzNm8W9E!fGaOFFIjlKx*iC0FOE2S3ZdsCpHLEd9Q6zJVbNPZK0a5mKVTJu1iaLz6sGsdqoW5iZycXTekg1Rxk*xFpqCa9FGU81Ql1ToQxW26QS97C2styXsBAy*E8XJ4oOaE7hpfUNH03C7eENsrkm7FNp1PSGjl4m8ZX1hkOaMcX1tZJ5JCZg9HviMuzTAG*JqBxGhxnGjGx78tBQL1NDK1hm2C4sjlSVBTqoLA6c0jEe7ZV64hvOfT7cg0XQ*n2vv17ydH35nQX893Cl5lnw*iVjtk4I30To$")

            ,("nuxhduuoh461@outlook.com", "ZqGmGppOGZ", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C554_BAY.0.U.-CipqsFehVdIoxKVP!xRqLrpxpbAfpkgMhfTKrF5bhFf0dSGZIRBg*UbvMfb83LPBBmbhQSZCOU7IhHjJSeSlZAYXPAC5c!PWWcWtzKum5LDWK*xt0qJRAE1AvqP4BPxF50fCe!ML8*iU2RDftjxS4GT6QPjab0*9ooe*Jo775*9OouswKCoy!AHEKqjvghEiBym3BMSYN1FPuaiqzHo65WPYfM8hGllxjofA1JKVCoo24n7v3eRm22zNRgZoWoB4oHIQfG0hZ44jSQff9ZN2aoMc7vioKhlRx!gj8V3waMO8Qf9vAqq7VWqh81mwO*vuzwKLbE16215UMNnhvYOo1Ez7ebeogAEnkhQTlj4h!yzdX5Mz!I1rjiCXgWnD*o55yK*M6uu9BY*IDV3ztQj758A$")

            ,("amlhapu7902@outlook.com", "cRueJyDCv", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C526_BAY.0.U.-CqJUxbUjAwec!l738DjXHHKVrFbaTLNdsp*gILm8PgMV1o9xXu!gIeu6*W8WSvFx9L6JW2zRc7L1DFXj1U2udydRNU7Q7jRhdzIRBvaZSWref4IcsU8Beun4!n30pcrcx5wtKMGOFE!J7pg1DfP73XNPTNGCkZXGLd2Cp8zQLEEPBh0HUSlw7Enp!ZvakEhbQQFLTa9DmHv0GN2oKSPicAmqxZ!bPwNfLN1nRbxDKuVtulzQ3SAv4!dJMigjXnLOw5Wf486qRyMY0Qv8rzjqulXbVC5h7EhZL!lClnMtaMXO1sejChT!i9PySig!Wmt1a!WXvQTwI!AdYQMAOEJsE9D7OlM7KC4Zj4EzVt1sqlB3YvYwM0uuVeOM3tVIvmfchKP8jsJXFtHjiA8yc!5y1HI$")

            ,("dmirwqdd2078@outlook.com", "RG1UsGxGQQkL9", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C502_BAY.0.U.-CnKnApndUv5xdIyDjXpgTupQXYKzv129apjb8tSDOAQg4BGXeGgN8yK8pp!krGQNtW1FJBetn!3i1C4yrymoTQrfT05xvNSKyNP7UCs!4hkmwWvFmEcTR4Jnxk1Qyk5UH!Go2eVRFSl9ffC3yf1gXSSdGbI6LkKlFjHpuJ3MRuJGm5*9hIV*Rk!fypaym0wqnY4O9y0LGoEX2q2R3ZhCE9JDRmQAJHeGUwMnMIYnnnrWAs25zfkAzOb7Ro*dL!JngFQFkY00DMzube6ofUwLF56rDgf1Mn69e9oC8jeFWogQ7lihWGrx4XLLnantMooWmVExcKdcCpotqX3aHGdBzaD!An6J1oDc*umQtZyZ1s1wYSVx516UN6sxSEr26JQbikpR84KV6J7LY*Z92WXdftg$")

            ,("xqbiuld7881@outlook.com", "rU8En6n8Ni5a", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C560_BAY.0.U.-CgpphhqO1lX7mAIeubccKQe5LkkxA*GQUAGQ85GRla332NxaHhELku9lDHdQL3eFaE!07nPKP3dNvCePQnxBPvugy4PQJZQqm7OMan1YkPbJv7y1e4A7VN6*OlyROcPN3MZEPjXytYZieFM7OUyxo8*m0f844RhT5TTfymuslW8Iqzuz55zNbxFvjbnrHnD8xFD1YIz49FY8pbAwBaJg5wEXNV0GAi9VgjH!KQReX6M7D393y9kmvUpDpB7QcqzbGiVu!63OjtGkuM4RyQJvr9K7s7S6Qoy6b9ahUbH6364w!3!7M1rJLedhTQg5872Lpwy8wHA4O6h9valJrvkAH0p6rmPQ*k!AQ*NnRdmZACbjeDCuOT4rmu*t5SnuF23BOAYU3tK5Qr9xYjDzpbKvpIU$")




            ("eyyhwufvuh388@outlook.com", "D1Jfuze1B", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C524_BAY.0.U.-Ch1!pLyCny!Uo!9SNU2vodni5aNSZUdGN!tAH2smJICi5KYagZ*A55qtw72YG2hetjw9YPjCmBuo3o27viFTUWBA0BseOv8Z2WSwYHS0k441sRlehQ7NXSFo6Ei*DHcufuEgC6U3UWf*uZq5UB!0aAC8tyPVTLwadgfkz9iGYQeqdfyccz5S53FJgVYe7OaqfM7Jfj1Qzd7uiFQ4tIOslDAEAq2vBfGxoSVzGggFHeRiEVO*zlGdAPBctmUlYDvFTEvNQwLEsWy8qvRVdHN5EXPdR0d9qcoLMDoaMP5VPX3xvpN0Md54EJJXvcmjJZHeqYQ4ZBdoklx5RHywNS1pq8OPyVfi8dmzTijdTKQr4ybWcdpskSrsQVd!t2401I5nXCqNkLOPx*iqLtvglJBwuno$")

            ,("awebiayj822@outlook.com", "ZWAwOr87kr", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C537_BAY.0.U.-CnJVRAh6U68vMSprddrIjPErtfvFzXC4JnPXD6w3omx5re7wqb62JWXof2VzCV3qhVWqEZbVHVReElsqY97OqlA1CZG6xoFjCW5L!qd6NV9jWFSih79EEDudr5y*hY0nvQX*NV6nYJiWxeTdlJyHq09w7ajvEKaGM0qMr9BpNQesvHPKID67tL7hj!C9ScMoKydrqu8XoFCLh76DRF7pMP5vW*7UW6MEiuQmcbWj74iH8V5w2!GkZpZG9lkLMtUOci1oLEI!IP79QUYZDz0!asa0PT7DUbaMBXXJCivmXAsc*of4wNbloCXeC!ByDD6YNTErXpbBpHIS427RsYPomsNKi6QuVc1LUpwpnVCfBEgtY6dO6fPYF!VKhdDVAEv*G4oXrso1t1YBummp8YrAeUQ$")

            ,("elheocrvmn480@outlook.com", "Pj2kfFSWn", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C511_BAY.0.U.-Cp8qz7Ny1IyMhThVKS81iAeR0BMASRK**QrFentMAjvXT*0z8OivDVKOp0Y1kMWl8XtDL89veclWT0Y98hIQ2C8PiDQT9591yh2SaPbc!zCA6vrGioDY04D6ucEdOXFK72ISPkW2HvEngzVWZxyHbKP1SOkZi65Quj6BdwZV5Ol0aHfuIoJF*jAaNRHUaerTSsWNlRRgH4FQ0mxB0U4NJfBLnMAaKL2rR3Sw!eybmkGwN2JpIvN0jCoukH9T3JTQKQqmB3PofOCx*Pb7xa4bStgqvg!wAms6iGnpMwjG!Li*3KZPUF05cwuHZSubQ8eRBlI77fgUzqeX8L6pVdwiZuQAClktJe98QZ5ec779flZXO9d*7EDoi1sheLnQxLR!!2RPrVxG3TR28KeSxcLVZMk$")

            ,("nfqbyapvdp7481@outlook.com", "Ec43hGeEX7xt", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C560_BAY.0.U.-CvFgI4enO3HGWWs!L80us0YT1cq3No3HqSjbjd!PiR7RqsaFPn7MTYSftXiIO4rj7LsCY0T5KSvY74Zxkn8YoT!GhjmbFoPNn3jLj9VcKsQyb2bDxvna7KMb9RKaSqLBEzbSxnv3LbjTAvpwHffiS*Jr5wYq4vcKFpg18hvV8Ce3qmetezqXCxvwfMbZaY4rcaB1weMzZQDtH*CjOnPm9omMRJhjzooT5bHObFSxhm2qynuesUCRHR2OlJ6Cye*Ki16o4BiqYqBIdEVuqFMienGWeNcTH!81BaXQccfC3WT8u3nhsu7StQRUCCSwL!yGukqav34a8yFu9wa2GRTBGscBszBQt5BN3AGbDJ21AtXFFJJCrWjz6MRtUxqHnuvkUTo7F69dBCGKU6NmFLQ3Z5M$")

            ,("gfbvbsp7474@outlook.com", "xqFpNs7OV", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C543_BAY.0.U.-CtxmRHbSj62v2HcYWhix*UwesDXz4P5ljoPMLKiSm9nq3JehgUaXeIg5kLMcolP6Hp3mRPeu5iJAZcOKBHUWMXAeT6uGKFkp9UfST9KxZYAmckg3xkxMHoBM6FM!BzPqDSAvXOLpwDoyaaSJxK3PeSKx6euJ!hEXHiR4ZyRSS7kbanJX4xTVuFZX2dzRLOJTyYfi1YQwwFDzC3tq67mkescQRX3JJNze9BsoOXQHFe2jn5pE1WlXg32Pz96HXRLpWVeM2pI*M2bL7HAf7A6D2w30b8t6rz8bE7WG5gpoMwNFXBYR*btE7GyPI28579r8odWIM1ehy*bRL6ATbzLoUBinALLlk6ralzL23BgPbeXEbiQ8w9QfibfOKNXSVrYCuoZERidE2ykFzfYh47czgaY$")

            ,("prxggzgmxl491@outlook.com", "w0hYAaTS07", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C547_BAY.0.U.-ChevWoNBejvdB2TqOt!aK9qaKRWBhOlmhofOwlqcgHLtPdjst1k4sDb0lADLXXocDNKYFY68zLQF8W2JhczQZmYIg6tKGBhBal4OzClmrb*dgfflLSHkn9mKMbqLxg5ZDnSSAfBpTmc4qj8orMyv1Cvo3Zjdn0EwboAzcPnDx4eABwcwS215SOS75VNvdWoK5nnqO5okMasVxCPp9By9mu!4YobuEm3NIaV8FRX7pnX7CKzQiA4bBdC3liRtlq!d5OnQc8OrZIhE!eiK9k6LLdTE2I4UqiUcCdBiraUFtL5g2rA0d!rSL2b!80fDz*buuu!o9YAvl8iLVwmbxQfCetzM6EjvhGIGMhF1SyqBrk4UVm6lg1NKZmmGoyawWofmBZFgBbJOuhMgCD7W9evVbqc$")

            ,("egwnasyv0660@outlook.com", "qKfNg0Fj4ok6g", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C535_BAY.0.U.-CiLiD!dI6xaXsueWN20o2XMGZCViYD!rG4x9W61lW7klLlRYZ2ar!G8UREohNpUdl8U7qzQrolrGM3tj*FIl*ZXLCuO!n8MoLyuMW3gPRAo4DUrZb7dc4mJnbdDHPNi81ydigiVoZRlArpBTyc2!QTaQoSI97R8snOBrhFIp6IO2*DvcOcDuQMH4nFfvtXg68i0MQ4fJSNqXwhAY86SWHX*K5N6H95*oq0rOUn8znUbnQgSBh5Z4!eaLpaGiRjf1FDzkLdGAT4a4OzynoD*46G0APKrGz!M4L*YOPfBEZs7sdFJRc1ItxpQzrzAjLNJFnObvWxdAWVhwAscGPEwbyeToLC!DY9XlpNVwvY*CHVZqXyCDHAwFpoGXyPMwno56HWz!nLZYH5stGNmzG7HXgMI$")

            ,("ctgbqzdt2412@outlook.com", "arZjiI9CIsU", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C559_BAY.0.U.-CkAEWe!F!STf4hUfJBeiifWc!JgNgVlcmUdg8wAh!hn1peB*Kykpgs2NPy!8wrp6uWzv*bMZfyHCTD2cC!*o485qFgOMTER05hTtiktGwBMeIGiALqD521AQkgVK*Hs7JAzijJWcMsKkkAwVMLuCAo9h!tk6v5scmygPFpXa7qSHh6!d8jYskRupqUJudKbMYQYXCYoI2k4ObVUoxaDVurEFmvPDXMadU1ArapB53k0jbUxBkTbX!xd810aUNGe2J5kfO6MSIGEG6FuTKMFaK4nWsuhk7Cn*pvAehyIUDr4bLkCOCKudI26jaU8krAVBVmudo0okmCjRSKRnyRlHapxUhewCw3oooLE2lFw*b4z0t7qNqLqwUaMOdbQ9*TS!p*MNWDmui0NA9WeSPv4I94g$")

            ,("zkoikcrhbn271@outlook.com", "Og4C6F4xJyn", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C507_BAY.0.U.-CrvrkXwlvZ1ijThk*U60tNnvKxoP10*q9POnvZI*mm8EMpx8*FBnunqNBE3mlclf1mWGjrfqACUHZ1fUsyb2zv3SRXqoXpOr01wtZOsXBtiRLeBZaj0mJ5f4Sg0L1qKr3noJi6EgQdgHT1Rq5xAjrxSyTpQehfJaJp8EaqPVmFQ*HMmI34FXhbhk2mB2Cvp6kxiADJ6GclLY8CzevaTETgn3pwL*ayp*NNJstsBkkfOjV5!Z6UwfCVUgRea2KksX9vTAo6ZSxN2pbsPr1OaBxhcsRGCTrxz1CkGYxy1TcSN5Zbiv7VUxo3AqDXWZEgJWYqRG9YcSDGCTKlwUQLyuE!XfwezNelsADZvfJpyWcHE!3!WPHaSOdr5htvjhr*IGKVogxm3e7UYj8yyvbONVz10$")

            ,("zkdlktno2219@outlook.com", "raiSQdbjdbbWw", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C504_BAY.0.U.-CgmN9vCC6oN80QJVGOoDKwPq9CX5dxm85m*CzTT*FSDUVe11huzAlGKoR5J1XrCg9Iclhz9FK8DXVycL1iHUXLhqB5bouP4zeKJ!v5*0V9LgKyOn3*xCtqb40gDRWKm3Q1DG49cRAUjMfNILUWZOoJ*kC7s!bwOOAHYFOUdQNH9AT!epnEsA4NRFsfoIVBV4B7bAVNpDL4vJ5S8fHy5SjhNdmLL2nukUrgyREwfV8FXWhcEcmzwLzUV1kwX9CiC3bL9jFS97lpJcrgErCoTDFunrGSaeQjd8h1I8jv6AjP7nlJRtXFTVi!vP7Khci9rYglv8DkkcFI5w4n*dgAB0zNvJVtFjnIdDGO*Z9rhKsihZhqYh2lQyTWBprb!byiKFPXgEG!N0uyTc9!TQXGMNP1I$")

            ,("epwznrkol727@outlook.com", "YSVfnFy5MJi", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C509_BAY.0.U.-CjWjNrs4WWWmNha*kRz*lTJwwhXdM2dEp8rn9mWgCkRVqCZFqSdvzuS*QCgUimQMsrCp6BbDTogCCKZ7i4t6JiDzZ!SfIPEkdGyXLPGT6xRDQHXq47fyZ9nL6!f6ysjYoPPagejOAW0n33UVfMpqwEnOYpjfRnQNcUpADWjXm47oJDd*Sir3aWkMvkEnc4BKZR!o28mMDdhads*7ixNbejEk6b2MwhSJ8kd8Qa03OjApasOG7WhLa!g*latxwNgTCaON53GtoaAFVyiW1!kB7lkX*d*EYcAjmym7tZQgmWr7I0kTYgzsZ60hx5ZnQa7Ibnqg3oPvm36hr979g6Fcvl6zFMODlhMBRa6R5tIdVg9mGtCdaKfNXkaV7W7Vux0RT6wZms8btqX4g5xiBWxzHIc$")


            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)