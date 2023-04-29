from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI


chat = ChatOpenAI(temperature=0)
tools = load_tools(["terminal"])

agent = initialize_agent(
    tools,
    chat,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.run("Who is the current terminal user?I would like to know the list of directories under that user's home directory.")
