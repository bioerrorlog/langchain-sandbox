# from langchain.chains import RetrievalQA
# from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator


# loader = TextLoader('./data/hashire_merosu.txt', encoding='shift_jis')
loader = TextLoader('./data/bocchan.txt', encoding='shift_jis')
# loader = TextLoader('./data/melos.txt', encoding='utf8')
index = VectorstoreIndexCreator().from_loaders([loader])

query = "メロスは誰ですか？"
print(index.query(query))
