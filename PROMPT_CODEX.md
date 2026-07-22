# Briefing para reconstrução via Codex

Copie o conteúdo da seção abaixo e envie ao Codex em um diretório vazio.

## Prompt

Crie um projeto Python mínimo chamado `ws-primeiro-agente` para demonstrar a
execução de um agente de IA com LangChain e OpenAI. Implemente o projeto por
completo, sem aguardar confirmações intermediárias, seguindo esta especificação:

### Stack e dependências

- Python 3.13, gerenciado com `uv`;
- `langchain>=1.3.14`;
- `langchain-openai>=1.4.0`;
- `openai>=2.46.0`;
- `pydantic-settings>=2.14.2`;
- `python-dotenv>=1.2.2`.

### Estrutura desejada

```text
.
├── chat/
│   └── llm_models.py
├── src/
│   └── settings.py
├── main.py
├── pyproject.toml
├── .python-version
├── .gitignore
├── .env.example
└── README.md
```

### Comportamento e responsabilidades

1. Em `src/settings.py`, crie uma classe baseada em `BaseSettings` que leia o
   arquivo `.env`, ignore variáveis extras e exija `OPENAI_API_KEY` como
   `SecretStr`. Exporte uma instância única chamada `settings`. Não use
   `load_dotenv()` diretamente.
2. Em `chat/llm_models.py`, centralize uma instância de `ChatOpenAI` chamada
   `gpt_4_1_mini`. Use `settings.OPENAI_API_KEY`, o modelo `gpt-4.1-mini` e
   temperatura `1`.
3. Em `main.py`, importe esse modelo e crie um agente com `create_agent`. Use o
   system prompt `Você está autorizado a ser criativo.` e envie um
   `HumanMessage` pedindo um ditado ou provérbio original, com sentido, sem
   explicação. Execute o agente, obtenha a última mensagem e imprima seu
   conteúdo depois do título `Output do Agente:`.
4. Coloque a execução em uma função `main()` protegida por
   `if __name__ == "__main__":`.
5. Configure `.python-version` com `3.13`, inclua `.env` e `.venv` no
   `.gitignore` e forneça `.env.example` sem qualquer chave real.
6. Escreva um README curto com instalação via `uv sync`, configuração da chave
   e execução via `uv run python main.py`.

Mantenha o código simples, tipado e sem abstrações adicionais. Não inclua
segredos, não faça chamadas reais à API durante a implementação e não adicione
testes que dependam da rede.

### Critérios de aceite

- a estrutura solicitada foi criada;
- `python -m py_compile` não encontra erros nos arquivos Python;
- importar `main.py` não executa o agente;
- a ausência da chave gera erro de configuração claro;
- nenhuma chave ou arquivo `.env` é versionado;
- `git diff --check` não encontra problemas de formatação.

Ao terminar, informe os arquivos criados, as validações realizadas e o comando
que o usuário deve executar.
