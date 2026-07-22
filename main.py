from pprint import pprint

from langchain.agents import create_agent
from langchain.messages import HumanMessage

from chat.llm_models import gpt_4_1_mini


def main() -> None:
    question = HumanMessage(content="Crie um ditado, um provérbio, que deve ter sentido. Pode se basear em provérbios já existentes, mas não pode ser uma cópia literal. Seja criativo. Não precisa explicar o provérbio, apenas crie-o.")

    agent = create_agent(
        model=gpt_4_1_mini,
        system_prompt="Você está autorizado a ser criativo.",
    )

    response = agent.invoke({"messages": [question]})

    final_content = response["messages"][-1].content
    print("Output do Agente:")
    pprint(final_content)


if __name__ == "__main__":
    main()
