class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
            


         
            ("malowbraamh1@hotmail.com", "iLcWHwen", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C519_BAY.0.U.-CnArnru1SUviNsvQiLHDfj4q5jG6tUK7FDoXKbOfO01njVf7IKorL3cZwH!cUq9EdZduBgQdJ*HupQ3DdmNBrryIM0dePuBNPG7ifdA4sukx3QSmNH0Lsb1Bl89HXibSYs4U*92F97JqxWTj7wPOYVGzdhHSaoZaq2DEAob4JreP*if5Jr*nZlEeboxAjARUwGJgEJFcp9GsTqrcp9EdpgERKIOju2krvUP9cZPm8ovL7xkDQd0R7jWEi!DJQHSntdj2!ZcPNpSNF6WDwpZ6e3c1b7VMzeWn6ACDQoA7RbTi!u1q4LnNAtNuPpM5vfXONgffMTQh5Z1LVFepf02iZu1TSoNBpMEQHTTQsRoVkCT7LE5pmY665DEEru7AKT4zhzfsWg5XM2lIP6hG3T8yuVi4GOJOhanfJMFSxcdlYyp6")
            ,("gantekneibfh@hotmail.com", "ZmrY01WI", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C553_BAY.0.U.-CmgqwQEfj6XzOyB9AwjZLAukLwo*chgDOBvBc7dcHQKuVmCnrs8tpDmKxXHW4wuLaCmgw*OGbrWUAqyGQZgtQta9YCc8pEXw8MzFk8H5PiLDQZctsGTszvhSzpvp94SdgFvg53j5DGuhmUsTwLBrNapRXGKbrdUblIMjyaLskScbT08oWrcipNrClgnvXSc5zFHIQJ53yuhV9tJKvF9fvEyCgU8BROQEzXsdEY2nreF9PmDs*m2i37XBMD4HR4Z5zEifAy30JlE5D0FJBo8JOxog1eeSMrqo7XAwj6*Z8pYHqFjvLD*yrxhHTgqVhKDVU6njsSV2XehgoRr!CKDjOs1zcU15rcLU0RjkLkTyqfY4El2tGKMMFK0AfcWH1cMxceF3EEfqffFrIdAGCx1QHz9*B*3IAdSBbGRdjUYa*m3C")


            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)