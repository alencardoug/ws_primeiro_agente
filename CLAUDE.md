# Instruções do projeto

## Objetivo

Construa e mantenha um projeto Python mínimo chamado `ws-primeiro-agente` que
valide uma chamada à OpenAI por meio de um agente do LangChain. Ao receber este
arquivo em um diretório vazio, implemente todo o projeto sem pedir confirmações
intermediárias.

## Stack

- Python 3.13 e `uv`;
- `langchain>=1.3.14`;
- `langchain-openai>=1.4.0`;
- `openai>=2.46.0`;
- `pydantic-settings>=2.14.2`;
- `python-dotenv>=1.2.2`.

## Estrutura

```text
.
├── chat/llm_models.py
├── src/settings.py
├── main.py
├── pyproject.toml
├── .python-version
├── .gitignore
├── .env.example
└── README.md
```

## Implementação obrigatória

- `src/settings.py`: defina `Settings(BaseSettings)`, carregue `.env` com
  `SettingsConfigDict`, ignore campos extras e exija `OPENAI_API_KEY` como
  `SecretStr`. Exporte uma instância `settings`. Não chame `load_dotenv()`.
- `chat/llm_models.py`: exporte `gpt_4_1_mini`, uma instância de `ChatOpenAI`
  configurada com a chave de `settings`, modelo `gpt-4.1-mini` e temperatura 1.
- `main.py`: crie um `HumanMessage` pedindo somente um provérbio original e com
  sentido. Crie o agente com `create_agent`, o modelo centralizado e o system
  prompt `Você está autorizado a ser criativo.`. Invoque-o, extraia a última
  mensagem e imprima `Output do Agente:` seguido do conteúdo.
- Proteja a execução com uma função `main()` e
  `if __name__ == "__main__":`, para que importar o módulo não chame a API.
- Configure `.python-version` como `3.13`. Ignore `.env`, `.venv`, caches Python
  e artefatos comuns no Git. O `.env.example` deve conter apenas
  `OPENAI_API_KEY=` e nunca uma chave real.
- Documente no README somente o propósito, a estrutura e os comandos
  `uv sync` e `uv run python main.py`.

## Regras

Mantenha o código curto, tipado e sem abstrações desnecessárias. Centralize
credenciais e configuração; não duplique a criação do modelo. Nunca leia,
imprima, versione ou invente segredos. Não faça chamadas reais à API durante a
implementação ou validação. Preserve mudanças do usuário que não conflitem com
estas instruções.

## Validação

Antes de concluir:

1. sincronize as dependências quando o ambiente permitir;
2. compile os arquivos Python sem executar a chamada externa;
3. confirme que importar `main.py` não executa o agente;
4. execute `git diff --check` e verifique que `.env` está ignorado;
5. informe os arquivos criados, as verificações realizadas e o comando de uso.
