from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know."),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])

llm = ChatOpenAI(temperature=0)
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)

response = conversation.predict(input="Hi I'm BioErrorLog, living in Tokyo.")
print(response)
# -> "Hello BioErrorLog, it's nice to meet you! I'm an AI language model. How can I assist you today?"

response = conversation.predict(input="Today is a holiday and the weather is nice.")
print(response)
# -> "That sounds lovely! Do you have any plans for the day?"

response = conversation.predict(input="Summarize our conversation so far.")
print(response)
# -> "Sure! You introduced yourself as BioErrorLog and mentioned that you're currently living in Tokyo. You also mentioned that today is a holiday and the weather is nice."
