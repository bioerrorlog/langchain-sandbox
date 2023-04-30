from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)

chat = ChatOpenAI(temperature=0)

response = chat([HumanMessage(content="Translate this sentence from English to French. I love programming.")])
# -> AIMessage(content="J'aime programmer.", additional_kwargs={})

print(response)  # content="J'aime programmer." additional_kwargs={}
print(type(response))  # <class 'langchain.schema.AIMessage'>
