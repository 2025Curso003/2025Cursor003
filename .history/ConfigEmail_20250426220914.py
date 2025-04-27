class ConfigEmail :
    def __init__(self):
        self.config = {}  # 存储配置的字典
        self.load_config()  # 加载配置

    def load_config(self):
        # 加载配置
        self.config = {
            "emails": [

            
            


         

            ,("mohakalurukt@outlook.com", "wdBEMLf9", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C521_BAY.0.U.-CkuemKT6ZYxinUEuFQNwUGgpBX9FklbU77SvyQuCjxFEuRvFBfPrUv87b9E25jBZ0!CKLafFY7sPPJpHzLAeUIBp7iLLQtYPBWHCG4lVnmkAh2xcWtUJfoNohQa6SDoFVNfeLED5N6bax3hUDkbsI3Hkn5AkukpsGM1!AT*vfX9HYMbGWxTm*A0XL2A7zwZxvEUU*Ktj3U5T*uMvUP52Is44AMU3s*A6SVmcAx6rdYuR!izRu5W6*fxTf3QnnHXYhjL08xOnjPKPopmRaJcmunEcWI9F0d3jix8Qo!ByKEQF2!hEf*YhyK*wztinGbjoMQmK*bOf32cGFQsCm*ALjumnLpvy6AUTpMj8x0KNJfodmtelTKqfBdt2hm0t2p9rurjTNW9gECTPVsaAW86U*E1nJJQ0s*7co0qfFyGwSGVU")
            ,("horthpapajos@outlook.com", "iTSn39eO", "8b4ba9dd-3ea5-4e5f-86f1-ddba2230dcf2", "M.C536_BAY.0.U.-CtepXbTQ6UR8KJ8FUMhvUVovMFh!kvWmfb8bfzRKV*8ixsZ86Xv5jHlnDjH5JJ*RnapY84xWPG3qsi1YShwIvJuKXqlYEmhhjXj2ObtYHe!dBb*JmIjzd8vqljofgwZZDi3SDefZbM01yBQWFvcO!QFTmoqY7XtBBqzkw1H7*R*Mw6OJY3UOHlySItNOoXaiZ0nDOx362pv5IaJb!OaIxx0RSQVJThqYbZEyaBuqOCzJ6h*O!l98JQ2qH0WC6xij1CBr1VqUtp6dK0AbPzvKy0yLMz5YBYRS7p6ZW7blehGXxpI3SpO82OKM7KuB941gh*vjc1l6*xhIYiB5uYmvIbLO!UM5iY3nNpDSJJ8TsEg2jez*6EO1wPTyw0uT3aDPCAWfqtJvU*neM02YU6zL1O5E9wEAz6UyEEjKFyUIjJ9a")

            ]
        }

    def get(self, key, default=None):
        # 获取配置项，如果不存在返回默认值
        return self.config.get(key, default)