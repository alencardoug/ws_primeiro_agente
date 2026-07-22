from langchain_openai import ChatOpenAI

from src.settings import settings


# Mantemos a criação dos modelos neste módulo para que configurações como nome,
# temperatura e credenciais não precisem ser repetidas em cada agente.
gpt_4_1_mini = ChatOpenAI(
    # A chave já foi lida e validada pelo BaseSettings. Passá-la explicitamente
    # evita depender de uma variável global em `os.environ` ou de `load_dotenv()`.
    openai_api_key=settings.OPENAI_API_KEY,
    # Este identificador determina qual modelo será chamado pela API da OpenAI.
    model="gpt-4.1-mini",
    # O valor 1 permite respostas mais variadas. Valores menores tendem a
    # produzir resultados mais previsíveis quando essa previsibilidade importa.
    temperature=1,
)
