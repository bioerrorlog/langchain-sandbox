from langchain.text_splitter import RecursiveCharacterTextSplitter


with open('./data/hashire_merosu.txt') as f:
    melos_text = f.read()

text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=1000,
    chunk_overlap=20,
    length_function=len,
)

texts = text_splitter.split_text([melos_text])
print(texts[0])
print(len(texts[0]))
print("\n区切り\n")
print(texts[10])
print(len(texts[10]))
