import requests
import time

# 你的 Wakatime API 密钥
api_key = "your_api_key_here"  # 替换为你的实际 API 密钥
url = "https://wakatime.com/api/v1/users/current/heartbeats"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

# 定义你想提交的活动数据
data = {
    "entity": "MyProject",  # 项目名，可以替换成实际的项目名称
    "time": int(time.time()),  # 当前时间戳
    "type": "coding",  # 活动类型
    "started": int(time.time() - 300),  # 过去 5 分钟的时间活动
}

# 发送心跳数据
response = requests.post(url, json=data, headers=headers)

print(response.status_code, response.text)
