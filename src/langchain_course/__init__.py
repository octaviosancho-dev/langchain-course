from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient


tavily = TavilyClient()

@tool
def search(query: str) -> str:
  """
  Tool that searches over internet
  Args:
    query: The query to seach for
  Returns:
    The search result
  """

  print(f"Searching for {query}")
  return tavily.search(query=query)

llm = ChatOpenAI(model="gpt-5.4-mini")
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
  print("Hello world from langchain-course")
  result = agent.invoke({"messages": HumanMessage(content="search for 3 job postings for an ai engineer using langchain on linkedin and list their details")})
  print(result)

main()