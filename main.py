from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from pydantic import BaseModel
from pprint import pprint
from typing import List

load_dotenv()

# Example 1: Agent with structured output


question = HumanMessage(content="Qual a stack do projeto?")
agent_structured = create_agent(
    model="gpt-4.1-mini",
    system_prompt="Você é um expert em python e IA. Responda com as informações sobre a stack do projeto.",
)

response_structured = agent_structured.invoke(
    {"messages": [question]}
)

print("Output do Agente:")
stack_info = response_structured["messages"][-1].content
pprint(stack_info)