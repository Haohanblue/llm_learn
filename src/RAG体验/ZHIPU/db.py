from langchain_community.document_loaders import PyMuPDFLoader
from zhipuai_embedding import ZhipuAIEmbeddings
import os 
from dotenv import load_dotenv
load_dotenv(verbose=True)
pwd = os.path.dirname(__file__)

# 定义持久化路径
persist_directory = f'{pwd}/db'

# 如果向量库已存在，则加载它
from langchain_community.vectorstores import Chroma
if os.path.exists(persist_directory):
    # 加载已经存在的向量库
    vectordb = Chroma(
        embedding_function=ZhipuAIEmbeddings(), 
        persist_directory=persist_directory
    )
    print(f"向量库中存储的数量：{vectordb._collection.count()}")
else:
    # 获取folder_path下所有文件路径，储存在file_paths里
    file_paths = []
    folder_path = f'{pwd}/data'
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    print(file_paths[:3])

    # 遍历文件路径并把实例化的loader存放在loaders里
    loaders = []
    for file_path in file_paths:
        file_type = file_path.split('.')[-1]
        if file_type == 'pdf':
            loaders.append(PyMuPDFLoader(file_path))

    # 下载文件并存储到text
    texts = []
    for loader in loaders: 
        texts.extend(loader.load())

    # 切分文档
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=50
    )
    split_docs = text_splitter.split_documents(texts)

    # 创建并持久化新的向量库
    vectordb = Chroma.from_documents(
        documents=split_docs,
        embedding=ZhipuAIEmbeddings(),
        persist_directory=persist_directory  # 允许我们将向量库保存到磁盘上
    )
    vectordb.persist()

# 检索问题
question = "iNode客户端出现“连接失败，请与管理员联系”怎么办？"
sim_docs = vectordb.similarity_search(question, k=3)
print(f"检索到的内容数：{len(sim_docs)}")
for i, sim_doc in enumerate(sim_docs):
    print(f"检索到的第{i+1}个内容: \n{sim_doc.page_content[:200]}", end="\n--------------\n")
mmr_docs = vectordb.max_marginal_relevance_search(question,k=3)
for i, sim_doc in enumerate(mmr_docs):
    print(f"MMR 检索到的第{i+1}个内容: \n{sim_doc.page_content[:200]}", end="\n--------------\n")