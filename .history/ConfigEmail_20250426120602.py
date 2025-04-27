class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
            
            ("mrygmozxgg8501@outlook.com", "Gq3FhBl6dqj", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C561_BAY.0.U.-ChGpbTiwOlfm6MCkaIR9UUoYF00F*h6i4ff0TYsmfyxTVegGEL!0O0MTaU1aoq4kmU6e6fx4kQbJSg5eOoM5B3ndZyKskuQ1Bal!bq72aQmru9LqS1SkdGEnFnM5USwHA5u2DN0*HosymENj*gZfrAEPuxGyvyQFuTSNdYJUdNNfOWExIZVphwPdZ42qCRZXxF8wjgh*Nb1ZtrsT1NeC7163sS7NzbFyRtXPtEFbuVfkQsQnBtIosyIvOYRQ!8QJ*twVHRIMMLANFgOuMDoBSQeSp9DJiwBAlmHH7rcBfNOtOtnyQNG*NfiX7B26ZCCChZH*bnU2CjGtDskwTtqx0tYDswAI94pbKN0tO3hw7dCdumRLII1E1HWpbGNxHlZlaSaJXyOdLbndNJzZ!YWO*fA$")
            ,("zjgdvfnqto302@outlook.com", "0fvF2GIdh", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C506_BAY.0.U.-CjpXSc6wU5yXPCnZFtajzr7LYPyQklVrW17Whwa4G!RlbILFJd6G!!NMyMFisqXcwx6a*QgRqlk1uvlBsPeMGqXSqCFIUv7pnPEvMfrLMQza6dX28GQY82XS7wA4i8mF2KMt4sVOCj6n4*or!TvuICagN1fhA8LNoOXGbce3hc8TvZBzgysYnnA7WlaQ75BQlGBGWARPYk9Qk1w7DXI4xbO!esVg373JACW4xuTkVUoO!xsD5BcRYRDPJT4qjCGI2s6L!Mb8a!lXmZv8d7zfzyePk61heGfxdXSb9oUDFEX9ra0dlYfhQwQRyXYyRciXLRXvGFM3fRA6da7LiCPYegzKYN1zmAu74KBn89v!IE5P6HEC5C6Z7d9OxT*UWDNy*qcryyqlkr67RF!cDOGyTtM$")
            ,("hdwtfjqm0774@outlook.com", "0w6hzBamrIv", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C540_BAY.0.U.-Ck8EleqO1TLV4GlH1K6Y7Bqenc1T!5h1me7i5RbtD1iYUWjEMDFyaXvJ*54Ai8F0YTJGkSslgzG29h6Lig8mVIwQlNXgH0SO3oGQk46pow!cTd0g74vHCTP5gGSijEj2DOkw70MyVv66bazXzonjARZpT7EvxTHRBbvpOxomSm7NKrLtO1apM53iky2LBKYKTEzrQ!seAy7*gSGnmV5yY2*XM98w!5Rs4G1RbZ9UYqj67bYvhgrsY57*M6grErYomrfEe2dtauFci5q!kKkiDMcHum3PGWvZ46GuEEbmxG3gfzUxRsY4FM5EVYd4szEnBvHfTmW5UBoFP*zSPMg8UgrOZ1RWVP5hXPLYbJLPRjWC6GaGHBvxj76auNeYa0fdLeQ!DHUWhDeft2CgHAm8Jd4$")
            ,("bqscdoodn507@outlook.com", "IZiC0PZQX", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C559_BAY.0.U.-Ct4zPKxazb8Qyeh*m43*3HeGr5*F02epOGvzq4dG21kqRYxpDHvSWqk93MsYbdDEIBzIep5T9I!IsBp6RRpqsnfTh8q*1FJldFPpM6bdaRG32VjCN08qxMgQQytfAmQ35!BWAqPxEFYxdwLPcIjPHqu2*gkscUz*kSHyy3BSFSZntVjflLQu!wrLWc8Nlw1f2X7cUKh9VSZ*Zke!3DILbMshlVlE5Yg3ObnfZBh89GgsuFuyGhaei9YV*cxqw52HxKmNoaeQUrfdGzdx0urO4*Jl4*xW87B6DNbMgv8XN6WafGBWDfUd!ldwwNgWVC4cZOdxdEo1QJsp48AhPXRLFYq!mINjnrKK2tBF8oDNjRg6mzMP13jmvhE8hy0eq4DobhqJqQLjIvin6nT1Xpa9SCI$")
            ,("mpopjao3916@outlook.com", "U0ZDSsiYvd99g", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C510_BAY.0.U.-Crlf*KhDnP!KmPKi0ql!VLCt2Zs33WsHAZS4!wVmDlgSfPoiDnZRBQXFiG1UQT1vJZtpTd5PnlzVgSo5XkdyrCpSfM!nLwPZ*In1TSkr8u*KyzAkx0Gjf!0TrUnyH44tZ39V427EzARWDv48XueouiYE7IpFDpWIFT*0gIlXdc8cHUO*zQi7XDnI2eyXuf3o6Hd3ADolgM1aA7JWKQCgHj*COU80Brj2*FEEqwmP6MpjMaD!gnNNQ9hGupPHFPl9QKCPVfbIRwBeJ6m!4RC5DWRyBd8N2c0D7HWJVPmFSxfJxrtaf1ZyQ2HVFSo4IygJDHrdz2qBK4!E7Fn*AhgfbFlIRk3mawVWauwaHkQZjh!y7YRf!mn22B6MEneOaICQgVYU1eFk*wznGDUv5ZrTuoc$")
            ,("paimqhnb5473@outlook.com", "w7ERnisrN5ZGv", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C501_BAY.0.U.-CqR2BHKPpRQ0I0OSQxEvqiI5bvSAxEmbOV*cgZLz9CZbxoTt*KdSeguod7AD6hYhz7FseWhYfGGGLy7F94eFvmpP1KEOp7gtyAxJeU4yaZ6eC2xsheo3cWjRfbiWXFqowbs37N4jWBrGO!9ubcgJ!Gmq1!MVnHfMtUrsOUg7Z!NMVFC5!8POvEa!pYg92K1wFkwd4*y2rJx3oUbeaCkMFhMBBOXX1Zh5mVQ!jdeBNFNsTIMlSU8x0OcBfnhzvnXnvyITvUF3!H5cCI81AcOb44g4HhabK4rg5ygpNnmla5P7Q4KTV2uVTEIUbWAibhm6xtqDm1kZeRJm4EISId3KJyfPQkwKynW9G4J7zqSy7RBfGULSVqjhEdF8ER2TmuSKNfSHBpePiws4!GsBfFk7AyM$")
            
            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)