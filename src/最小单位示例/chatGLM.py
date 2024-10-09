from zhipuai import ZhipuAI
from dotenv import load_dotenv
load_dotenv(verbose=True)
import os 
# 获取单个环境变量的值
api_key = os.environ.get('ZHIPUAI_API_KEY')
client = ZhipuAI(api_key=api_key)  # 填写您自己的APIKey
response = client.chat.completions.create(
  model="glm-4",  # 填写需要调用的模型名称
  messages=[
    {"role": "user", "content": "作为一名营销专家，请为我的产品创作一个吸引人的slogan"},
    {"role": "assistant", "content": "当然，为了创作一个吸引人的slogan，请告诉我一些关于您产品的信息"},
    {"role": "user", "content": "智谱AI开放平台"},
    {"role": "assistant", "content": "智启未来，谱绘无限一智谱AI，让创新触手可及!"},
    {"role": "user", "content": "创造一个更精准、吸引人的slogan"}
  ],
  tools=[
    {
      "type": "web_search",
      "web_search": {
        "search_query": "帮我看看清华的升学率",
        "search_result": True,
      }
    }
  ],
  # 拓展参数
  extra_body={"temperature": 0.5, "max_tokens": 50},
)
print(response) 