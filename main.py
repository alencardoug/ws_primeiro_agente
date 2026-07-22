from pprint import pprint

from langchain.agents import create_agent
from langchain.messages import HumanMessage

from chat.llm_models import gpt_4_1_mini


# Colocar o exemplo em uma função evita que ele seja executado automaticamente
# caso este módulo seja importado por testes ou por outra parte da aplicação.
def main() -> None:
    # HumanMessage representa uma mensagem enviada pelo usuário ao agente.
    question = HumanMessage(content="Olá! Dê um oi curtinho mas criativo.")

    # O modelo já foi configurado em `chat.llm_models`, inclusive com a chave
    # carregada pelo Settings. Assim, este arquivo não precisa de `load_dotenv()`.
    agent = create_agent(
        model=gpt_4_1_mini,
        # O system prompt define o comportamento geral do agente e tem prioridade
        # sobre a mensagem comum enviada pelo usuário.
        system_prompt="Você está autorizado a ser criativo.",
    )

    # O agente recebe um estado contendo o histórico de mensagens. Mesmo havendo
    # apenas uma pergunta agora, a lista permite adicionar mais turnos depois.
    response = agent.invoke({"messages": [question]})

    # A resposta contém o histórico atualizado; a última mensagem é a resposta
    # final produzida pelo modelo para esta execução.
    final_content = response["messages"][-1].content
    print("Output do Agente:")
    pprint(final_content)


# Executa o exemplo somente quando `main.py` é iniciado diretamente.
if __name__ == "__main__":
    main()
