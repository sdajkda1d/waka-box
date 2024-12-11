import requests
import time

import os

api_key = os.getenv('WAKATIME_API_KEY')

url = "https://wakatime.com/api/v1/users/sdajkda1d/heartbeats"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

# 定义你想提交的活动数据
data = {
    "entity": "waka-box",  # 项目名，可以替换成实际的项目名称
    "time": int(time.time()),  # 当前时间戳
    "type": "coding",  # 活动类型
    "started": int(time.time() - 300),  # 过去 5 分钟的时间活动
}

# 发送心跳数据
response = requests.post(url, json=data, headers=headers)

print(response.status_code, response.text)
