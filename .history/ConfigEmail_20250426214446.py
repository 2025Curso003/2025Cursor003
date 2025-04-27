class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
            


         

            ("rouchhaseyc2@outlook.com", "boMPf4nU", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C545_BAY.0.U.-CrJ2aWSnKtyAKDeQtE4u8MEUx6O2PmRkCjUYQoIBRGs!6SShIk9JIOFoNFMtW*NLH*Fp1i*tCsqKRe4sodXZgvtwzaqXqhpeS8IYi8IilWk1NdgdpqGZZ1sL6mNSW2PqIEy*DIcT5CTlC*xDy4v3HqY*f*7YmtYjJFGOhdcUXgUw!unaGBT4mn*WDq6ksmTgokVzC36y74DkLui4P!J1D7NAeYytsZOndTGEJhMMGsHVMZHwI0kXu0uDLUdu27DLzeZ2cb1gl!eJgkGQt9QHPWk*s9l!DQ1mOROpSkY0z!0fXd2mhyC8fFX8Bz5kymVXaJuGzFhqknqZiqlynxSjxqBLwNkbOQ3DJImvVXUzq*tyma*pETxm2303oyMehh22F!IGVF7IRcIcnNqv3WU8jIAvSAHyKZ7cUrtY1LcPvy55")
            ,("yaaristrand9@outlook.com", "Lyhqbecr", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C555_BAY.0.U.-CmX2dwEGqZbFIVhOzCFzpSJDc2KjZV19BMKt8*dw!V5dmKiBBMXR6Nr97csTpdS4YvSAbCBjnM7ia9dCw6KMawGtmXcaDbiTfFyTHHScaMvFPOc20B4Rvpzh05Sh28M*Svl5JmS59H4KeJHE18ogflAfsutjDYpZwOsudYZM2h1ZMUKvuxfxW46q77SGg2w3V2w*FsIXLH5bb7bxp3aZLPKynMKCVeERdB1NofyNlaiyNKgXNnC6M4*6XPix5*CgxPQn0Z7vtuMwm*kTxXdsGDyTuk*qTZARm3fNPh4Vx85WqKnuGiRofRih9sM3JMRali8rZMCb7aztilkVxvtVDG4Dpn5icRE6!qIFam!hO2G7rVJAGVBcaHdZx5siQW0KZPKISejsL8LeMjq*j3tZP3o$")
            ,("diacoweltz85@outlook.com", "DIXRfgZ6", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C553_BAY.0.U.-Cl4!M98Ce9uSyYi*n!t8xLnqo9i0CDehk0GfrPTZ8o5yCi1cay6DvaiD6PHWM!2YcEdzOPGesoFbLUSaU3J6*R0klu6j9eKDtuu8DSFtaoBE*4Q5nA6BU1jTT*oyoHeFUlq4wpVzF8Xcgob515PsHFcojVNVrkW7KEZLCenx481t4KhD4!j2aESVdUdFawb2AOO946dHeXmLBwt693wRqXofj2CBs90NKZKiPY!4!FhTlthBOBzaYOixNzo!y1QG9S!2yz4Wsq94a31w7LMLkRcCY!pAx5zFRF*ejn2pP!CAJQ*bemGxZGs6Fy5EZNMVzFleXGNCXeXgvTYlBT1TUsufuVo0tGRipyk7YNE*xllAsw6YuTCbsnRcloRW8tJIa39DyxjQXG1hZWVWBJx1AjtYBEASk9wbtuLIaoezMG*o")
            ,("yoskedaker23@outlook.com", "BRnvQRCD", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C530_BAY.0.U.-CjnqtOX7jfQgl3gL*biu2lKMBO!UkL7Mi7CzMZu1C*z43V5CXi*03Nw8KtHbp!ozxlppCeNps74Tvcnt2Lf7LPV!HxrfgfYSdbkOQpKIFMRit6zGPE1iTKQpG8wSUoV2BObpY6Cv9POLbfkIyEUa3WH6l2oG5xvNP6tH8NHfSQzqDU*55VwBBjpkRmNXKzOKZn1Jq0JMTJbOgkeVryesGiMskyUX1*on*0Zusp2YFp6E9XN026tRz6lS9jJ0PCnTqL02Yya1zzz0qqdlKyONZcXE94PhK03SC2yd8RkA*HuSqOAP3kFm*y24*pDAU2!5Ol7Bnij8747McxdXNQney41E2y2Ddt988GNRlTVzVX8lTembcXZYCBJlVmHrsIDLIcm3Ot58RTOpwpERUr1pGQI$")
            ,("buderbennonl@outlook.com", "ave97vQI", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C507_BAY.0.U.-CmuADOdJws0Jpge6PKx*OPf*HRxn*mb1okMeHRutDIFPmzBKyoJ2I4gQ3XSdzblWvwTDoDJfjljFXfFzfWSTDRC5p1FBwzp3m3IIcRktCOvzeXcP9iNe6KdkibdcJCBPaORRMFEGkRSzkE2eXuPmDjHrPJo7oXxR2nD14SJvC1ih4OlS8R8MprU0nX0Mon7xtd8WvW8mPLErWFVvVHSWZ8l2D*7IVhX09c0SmyTktYn7zcBM6ahVt6sgRC3Ot7ZgDxCgqNtFE3EYGU9RUdsYXSIqhg58jfG67tQ1kW3vpCLer61mt*IeA3im!94sdlmuO!WheROnTqaCTkBrJLHTBULAOAAt!yCqx5PeNzhb5sXA!!ajmQWf0PRTM0mpSj2ehqb9lACdf!wQ80xCSonbORf9!mSTOzt64eeyxo!mL69B")
            ,("kenelreznymh@outlook.com", "nUw66CGE", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C531_BAY.0.U.-CurQlT3dWo*33mcA*JBCjE*X*MpV0*J6xC0!Kpc9FM1pOCO8UEKUtUg8avg0jccJMb!fpLgpBYUQfZ*sFqam5mkO7VjbG9esVBP!dDSTK0bgd2EMWqDMXkAfTJ9!BBlxgozN9kXcbBbax4OFnQq12ZbOYLZ5LQko8z3ZDDkUpqQdiyOi3HfXMPZcbpxv7YZpP18FMkaxwTbV!AFlogtm8DFWDhhEziVAgJlAkeaZYV7oC!KUVpFKDB0iWb!hpwo!Dq4wcj3fcVeAvD!tNVF*eqCXaVncTppWIspTA6!uWxgBXBjA8GLKkeTgm1wu6LlUBMb1d64mDYg!*uVBrNeHaAtHPlG27!xj7A6sAuPyynUuAxExuHnULM5K6cKV10vbql!uh5JIUtpl6woESrPSEQOBZa9p9ls3LK5urhIvRXKE")
            ,("klodaganasoh@outlook.com", "GZlhNlRN", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C540_BAY.0.U.-ChvTnjNc5IawmPV*AkIxmpMQ26hdFxhlMl27IQE3nX1PeMDPMq62Y8WXjq4pVgAEupTKAo8YwZPnBR5nPYKHiyFEjNe3UM2pdtfvrRHalM8aOpbniTSwByKTxyn2A7vU7Zxk9w1jTZkdsrsF5uootwQ!nNgpK1HodOf31JvVEMKeuE1mx*j6IdQb7zBOSjLPVrbhGTYfyMCCHuDB!ERUwGJTQQKuy*YzFFdzl!h1HvQI5xDGbIcfh6Z8RvJ7Sn4CovJo!Jd!kZ6XOLPMBPNR3EmqA6qCDS*DMa7ztF7Md0aqPxBGI7lBddMzto!VrYiZveGJ1nqchN*AKtI81ea!t*aLgD6vZ13Rzwlk2zQPU3N1Fcg3EkPjFqhS6Zv6HkuY6n1aZYrRthtrPh3ZdFGuDYI$")
            ,("obuchgeike3x@outlook.com", "bkPpTLjV", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C523_BAY.0.U.-Cl5RLz6ADoMnmYd3w*zr5!*nhY2DcLu0teIsUF9tqTOadJMjjnW4J3wmV5js4jiBt4lg4igmWgANCHluxX2oqOd7Km*mrN4kBhgPi27tALd0SovgKRmlNST99B5C0x4UVE*Xcx9Kt9cEGQJBVAkfXWQjXnjX6fybdq*mJlUXTiNVbAiE0lnMTZ5M75W1Ow0Vyv8fLJZom*9OJzf!cd4Ef2DfR*7uZUo0p1EPugIBb!Ylpuha8gxlrM9xYbfN8adFIJzbZw!*JVNLOtvRy2Yz84zZrGg*AamfWIMbo3Wd3fol1mjn7mKxTPSfO5Azw3ltZDRvr19FIRaI3p0AOg0hkj8JAo8nIy0jh7A3lCLLJXWwLyt2wqeR826RX0ni0srYSbZFRmFclYCJmVNlUf!l1NQ$")
            ,("najibbenuseb@outlook.com", "ZMBsrG8R", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C533_BAY.0.U.-CkHm3ZjCEw0LuAyuORct08V0gWAz9k97jKDmsvoUCH*3LScXoZwbaMCXBhEmEy1XRgDaGu7lcUOFzqqoF0B6WIOhQKL8vZ2*0Avd8qYem5IdaRl6AmBI3gNavPp2iYcsJ6X94hDru2AxL4sYfTVl7gXrYFGJ!y7PT35RSN3SfgTuwxpSLLiIbh1bg!f8jpjgn42MIrchmk65sXaz6eZ2zplJiisPZkLCypsTpbRO*m1RK7GxRcfH!FBItcxQ8wWIklNVsSPouGDenZiqoqGLri!leIdQLofTB3vfsfrrhchoXc6TBvFlBRblhIwpmLR1dI3SDUsUkZrHL8wj40MztLsWaqy94L1FYzgjPpBkLG5TcsODoGtfQ40RD0UFd1bBSsbptGS!0vDHPfGCt5u6o*dkTG1Qs5JRnrvfLji9o*a5")
            ,("cartesheark9@outlook.com", "Zdoa5cSp", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C510_BAY.0.U.-CsJkz3FFIkAcMoNBKtg2na7SKgCKDdqKKnkfYggKpQbNBacFResql9ZPVSCN4p6wxPRgm49U9YixMw3hmY4O3mj0954XZQhitReRe0CDGatSyNZluI5KzsUlAm3ANGblOCranu6Qw2sF*U64iLApbJxWfXzjieocmdHJrs5HLDJ1kvbzunNLWSBveESNwl*L4iwhZ2nYwuewiBf9iZcGwOglxUP53QTWVoXM28TqEs3tGO4yfhws!rrVn598p46JwZxdnP11FCiOVrHUQ1HC3OY61tTFGkkmoADlFiesvjoXigYlLEvCilqzCJGkzyWQkXxUAjLhXnmavE7DP7LSXwpZUD!BGj6*0JcRapGtpFPeWEDUHUCMtYt!0ThKfTz769g6!dXHqsDYWu6MEawSfjk$")


            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)