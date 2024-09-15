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
while True:
    # Get user input
    user_input = input("User: ")
    # Check if user wants to exit
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    client = ZhipuAI(api_key=api_key) 
    response = client.chat.completions.create(
        model="glm-4",  
        messages=[
                  {"role": "user", "content": user_input}
        ],
        temperature=0.95,
        tools = tools
    )
    # output ChatGLM’s response
    s = response.choices[0].message.content
    print(s)