import requests
import time

# 获取github用户信息
url = 'https://api.github.com/users/judai39'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers, timeout=10)
print(r.text)
