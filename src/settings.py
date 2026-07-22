from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # O BaseSettings lê as variáveis do ambiente e, com `env_file`, também
    # carrega os valores definidos no arquivo .env ao criar `Settings()`.
    # Por isso, não é necessário chamar `load_dotenv()` separadamente.
    model_config = SettingsConfigDict(
        # O caminho é relativo ao diretório de onde a aplicação é executada.
        env_file=".env",
        # Permite que o .env contenha variáveis que ainda não são campos desta
        # classe, sem provocar erro de validação.
        extra="ignore",
    )

    # Não há valor padrão: se a chave não estiver no ambiente ou no .env, a
    # aplicação falhará ao iniciar, em vez de apresentar um erro apenas quando
    # tentar acessar a API da OpenAI.
    #
    # SecretStr mascara o valor em logs e representações do objeto, reduzindo o
    # risco de exposição acidental. O ChatOpenAI aceita esse tipo diretamente.
    OPENAI_API_KEY: SecretStr


# Centraliza a leitura e a validação das configurações. Os outros módulos devem
# importar este objeto e acessar `settings.OPENAI_API_KEY`, em vez de consultar
# `os.getenv()` diretamente. Assim, não dependemos de alterações globais em
# `os.environ` feitas por `load_dotenv()`.
settings = Settings()
