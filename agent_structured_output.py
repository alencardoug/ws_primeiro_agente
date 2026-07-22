from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from pydantic import BaseModel
from pprint import pprint
from typing import List

load_dotenv()

# Example 1: Agent with structured output

class CancerInfo(BaseModel):
	tipos_de_câncer: list[str]
	quantidade_de_sítios: int

question = HumanMessage(content="Qual são os tipos de câncer, se fossem tratados em sítios/conjuntos de tratamento em um hospital oncológico?")
agent_structured = create_agent(
	model="gpt-5-nano",
	system_prompt="Você é um expert em oncologia.",
	response_format=CancerInfo
)

response_structured = agent_structured.invoke(
	{"messages": [question]}
)

print("Output do Agente:")
cancer_info = response_structured["structured_response"]
pprint(cancer_info.model_dump())
