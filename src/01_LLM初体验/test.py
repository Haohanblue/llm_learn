from dotenv import load_dotenv
import os
import requests

import json
# 加载 .env 文件
load_dotenv(verbose=True)

# 使用环境变量
api_key = os.getenv("API_Key")
secrect_key = os.getenv("Secret_Key")
# 填充API Key与Secret Key
url = f"https://api.gptsapi.net/v1/chat/completions"
payload = json.dumps({
        "model": "gpt-3.5-turbo",
        "messages": [
        {
            "role":"system",
            "content":"you are a chat bot, talke with the user please"
        },
        {
            "role": "user",
            "content": "I love SWUFE"
        }]
    })

headers = { 'Content-Type': 'application/json',
           "Authorization": f"Bearer {secrect_key}",
          }
response = requests.request("POST", url, headers=headers, data=payload)
access_token = response.json().get("access_token")
response_dict = json.loads(response.text)

print(response_dict["choices"][0]["message"]["content"])