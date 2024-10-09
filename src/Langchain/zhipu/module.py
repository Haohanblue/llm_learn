from zhipuai_llm import ZhipuAILLM
from dotenv import load_dotenv
import os
load_dotenv(verbose=True)
pwd = os.path.dirname(__file__)

# 获取环境变量 API_KEY
api_key = os.environ["ZHIPUAI_API_KEY"] #填写控制台中获取的 APIKey 信息
zhipuai_model = ZhipuAILLM(model = "glm-4-air", temperature = 0, api_key = api_key)  #model="glm-4-0520", 
print(zhipuai_model.invoke("你好，请你自我介绍一下！"))
