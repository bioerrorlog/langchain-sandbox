from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
# from langchain.text_splitter import TokenTextSplitter


llm = ChatOpenAI(temperature=0)

loader = TextLoader('./data/hashire_merosu.txt', encoding='shift_jis')
# loader = TextLoader('./data/bocchan.txt', encoding='shift_jis')
# loader = TextLoader('./data/melos.txt', encoding='utf8')
index = VectorstoreIndexCreator(
    # text_splitter=TokenTextSplitter()
).from_loaders([loader])

query = "メロスは間に合いましたか？"
print(index.query(question=query, llm=llm))
