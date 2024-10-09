from zhipuai_llm import ZhipuAILLM
from dotenv import load_dotenv
import os
load_dotenv(verbose=True)
pwd = os.path.dirname(__file__)
# 使用智谱 Embedding API，注意，需要将上一章实现的封装代码下载到本地
from zhipuai_embedding import ZhipuAIEmbeddings
from langchain.vectorstores.chroma import Chroma
# 定义 Embeddings
embedding = ZhipuAIEmbeddings()
# 向量数据库持久化路径
persist_directory = f'{pwd}/db'
# 加载数据库
vectordb = Chroma(
    persist_directory=persist_directory,  # 允许我们将persist_directory目录保存到磁盘上
    embedding_function=embedding
)
print(f"向量库中存储的数量：{vectordb._collection.count()}")


from zhipuai_llm import ZhipuAILLM

# 获取环境变量 API_KEY
api_key = os.environ["ZHIPUAI_API_KEY"] #填写控制台中获取的 APIKey 信息
llm = ZhipuAILLM(model = "glm-4-air", temperature = 0, api_key = api_key)  #model="glm-4-0520", 
from langchain.prompts import PromptTemplate

template = """使用以下上下文来回答最后的问题。如果你不知道答案，就说你不知道，不要试图编造答
案。最多使用三句话。尽量使答案简明扼要。总是在回答的最后说“谢谢你的提问！”。
{context}
问题: {question}
"""

QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context","question"],
                                 template=template)

from langchain.chains import RetrievalQA

qa_chain = RetrievalQA.from_chain_type(llm,
                                       retriever=vectordb.as_retriever(),
                                       return_source_documents=True,
                                       chain_type_kwargs={"prompt":QA_CHAIN_PROMPT})


from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(
    memory_key="chat_history",  # 与 prompt 的输入变量保持一致。
    return_messages=True  # 将以消息列表的形式返回聊天记录，而不是单个字符串
)
from langchain.chains import ConversationalRetrievalChain

retriever=vectordb.as_retriever()

qa = ConversationalRetrievalChain.from_llm(
    llm,
    retriever=retriever,
    memory=memory
)
question = "iNode客户端出现“连接失败，请与管理员联系”怎么办？"
result = qa({"question": question})
print(result['answer'])

