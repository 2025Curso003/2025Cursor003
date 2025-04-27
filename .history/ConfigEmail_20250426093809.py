class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
            
           
            ,("ouppzkaiyl3820@outlook.com", "vQVqu61vAYZA", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C528_BAY.0.U.-Cl1Zqwe3MyNV!ThGFWfZGevDi9U2rDCCRukK7ldlHuJ*jU!VDYC3d3o8Eoa3Hg0Xv9kqJoR7Hd00QBX8idPmpSSkoVET0L5UMe9TKDbmafJq!T!6vUCPsxaPYvLNu!NHo3J*D2b7kntd4NOB4vslYAeL1McL9VhtWGubvjDi!pJfslYtlgMcSZHSeTEZNMVjQ5Yy21coGExugB*A39wrhcZmkvsmPpQjB5gg!H6c1s0pigbz4Z8HgJofA0aM!t*mpo0hOTLjR!4GbYbQgsz2ne!5AtbtQ6tJexlu6BBtlAv7Fw62MdYlTjOhhpCGnciRKeECpBdj!rf9QTHBxB!kqI6Qb8TQbxsxB6V1nPCHJIey9i8Up!PDE*oPg6p8kqvTV3U5FpnXjkZ0IB5SCoMszhw$")
            ,("ykhdwyxt0767@outlook.com", "j1meZz2IgatU", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C524_BAY.0.U.-CqXbew7foAgtcU3Zf5L3O9fhhKlJXs2Xf3vbGhSZLyVXetfbukrf9OrmlnoHs3L1P006Jj7dQqPFpKsgYOF4O*PIqworc0d7zh0iAwXzbCn!mFYygpEIufZKcro8vm5Mm05LoqoUjdvefO3pNYQaQEdFYNndFG4YZA7HjhZhuRjeYTwhaFC!rg5GwwGmVJ5thnADoANoNx8xoI6FFBGiK4q1eq6FMmXF72l7MINhIRFVaWSFcLl1gYERHNkLasMqbgkS3vMbD50VtaD3DxgvLgNiH6OuHm*vAuwn0wtdsCdmeUnwoIO51nmOsLvea5BGd!aFrfo9*16UCtq*s5vw4RGjAOm4Wz*FjL*nT1mY*NAAtas8C8qMjEO1qdo!n1xm10svxW1qe0!cXircmmcO7J8$")
            ,("zinbpdatn937@outlook.com", "pd05nyfCsJSqA", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C516_BAY.0.U.-Cp3tZ81v7dkMOO!xEuWbvcgcd7HDKCD*MEtpSUR9ThNGPybX4kYdj6tN7*wnds8UWas0AX0xjoK!tghiHtH6f1ZCJ2Vws3Drv98LIOML3Ktseo4b5CRl2BsVAX!PKuxZ45vXtjhFke!uwriYXzD0RMp8eFfe8MM3kW7AHgP6w0ib*4qsVxSBUI782aJWHDF*UsFwWwxlK8bq8RV1tsjKLzadAu0iON6lexezF53AggoqvepET8aAgftGTl4HqseU*3KmDwJ23dTBNQX1m0U*gQJ0ynMnI!als1azMNyxP4vuq9n6Lfwa3g1dv02!D1xPGVqxnwoY!efTL5c1w!eg!0cYb8IBGKSvufUAKoScxIqT!OaqxaFC*lzX8wRNb1qTtvFH9lL0GMND*KPY5jYf0H4$")
            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)