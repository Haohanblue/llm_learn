import os
from zhipuai import ZhipuAI
from dotenv import load_dotenv
load_dotenv(verbose=True)
# 获取单个环境变量的值
api_key = os.environ.get('glmapikey')
client = ZhipuAI(api_key=api_key)

messages = [{
  "role": "user",
  "content": "中国 2024 年一季度的GDP是多少 "
}]
tools = [{
  "type": "web_search",
  "web_search": {
      "enable": False # 禁用：False，启用：True，默认为 True。
  }
}]
response = client.chat.completions.create(
  model="glm-4",
  messages=messages,
  tools=tools
)
print(response.choices[0].message)