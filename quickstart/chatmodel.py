from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)

chat = ChatOpenAI(temperature=0)

messages = [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="Translate this sentence from English to French. I love programming.")
]
response = chat(messages)
# -> AIMessage(content="J'aime programmer.", additional_kwargs={})

print(response)  # content="J'aime programmer." additional_kwargs={}
print(type(response))  # <class 'langchain.schema.AIMessage'>
