# Primeiro agente de IA

Projeto mínimo em Python para validar uma chamada à API da OpenAI por meio de
um agente do LangChain. O agente recebe um pedido para criar um provérbio
original e imprime somente a resposta final.

## Estrutura

```text
.
├── chat/
│   └── llm_models.py   # Configuração do modelo de linguagem
├── src/
│   └── settings.py     # Leitura e validação das variáveis de ambiente
├── main.py             # Criação e execução do agente
├── pyproject.toml      # Metadados e dependências
├── README.md           # Visão geral, instalação e formas de reconstrução
├── CLAUDE.md           # Instruções persistentes para o Claude Code
├── PROMPT_CODEX.md     # Briefing para gerar o projeto com um agente de código
└── .env                # Chave local; nunca deve ser versionada
```

## Documentos para geração do projeto

Este repositório contém três documentos com funções diferentes:

- `README.md`: explica o objetivo, a estrutura, a instalação e a execução. Ele
  serve como contexto comum para uma pessoa ou para qualquer agente de código.
- `CLAUDE.md`: contém as instruções persistentes que o Claude Code usa para
  entender como o projeto deve ser criado e mantido.
- `PROMPT_CODEX.md`: contém um briefing autocontido para solicitar ao Codex a
  construção do projeto em uma pasta vazia.

O arquivo `PROMPT_CODEX.md` também pode ser renomeado para
`PROMPT_CLAUDE.md`. A mudança de nome serve apenas para deixar clara a
ferramenta escolhida; a especificação técnica funciona para ambos os agentes.
Ao usá-lo com o Claude Code, peça explicitamente que leia o arquivo.

### Combinações recomendadas

| Ferramenta | Arquivos | Forma de uso |
| --- | --- | --- |
| Codex | `README.md` + `PROMPT_CODEX.md` | Peça ao Codex que leia os dois e implemente o briefing. |
| Claude Code | `README.md` + `CLAUDE.md` | Inicie o Claude Code na raiz e solicite a implementação. |
| Claude Code, alternativa | `README.md` + `PROMPT_CLAUDE.md` | Peça explicitamente que leia o prompt renomeado. |

Não é necessário usar `CLAUDE.md` e `PROMPT_CLAUDE.md` juntos, pois eles
descrevem praticamente o mesmo resultado. Usar apenas a combinação indicada
reduz repetição e possíveis divergências.

## Gerar o código com Codex

1. Crie uma pasta vazia para a reconstrução:

   ```bash
   mkdir ws-primeiro-agente
   cd ws-primeiro-agente
   ```

2. Copie para essa pasta somente `README.md` e `PROMPT_CODEX.md`. Não copie os
   arquivos Python existentes, pois o objetivo é deixar o Codex criá-los.
3. Abra a pasta no Codex, seja pela CLI, aplicativo ou integração com o editor.
   Se estiver usando a CLI, inicie-a a partir dessa pasta:

   ```bash
   codex
   ```

4. Envie esta solicitação:

   ```text
   Leia README.md e PROMPT_CODEX.md. Implemente todo o projeto descrito nesses
   arquivos, valide o que puder sem chamar a API e informe como executá-lo.
   ```

5. Revise os arquivos criados e autorize a instalação das dependências caso a
   ferramenta solicite permissão.
6. Copie `.env.example` para `.env`, preencha sua própria chave e execute:

   ```bash
   uv sync
   uv run python main.py
   ```

## Gerar o código com Claude Code

### Forma recomendada: `CLAUDE.md`

1. Crie uma pasta vazia e copie para ela `README.md` e `CLAUDE.md`.
2. No terminal, entre nessa pasta e inicie o Claude Code:

   ```bash
   claude
   ```

3. Envie esta solicitação:

   ```text
   Implemente por completo o projeto definido no CLAUDE.md. Use o README.md
   como contexto, faça as validações locais e não realize chamadas reais à API.
   ```

4. Revise a implementação, crie o `.env` a partir de `.env.example`, informe a
   chave somente nesse arquivo local e execute `uv sync` e
   `uv run python main.py`.

### Alternativa: `PROMPT_CLAUDE.md`

1. Faça uma cópia de `PROMPT_CODEX.md` com o nome `PROMPT_CLAUDE.md`.
2. Coloque `README.md` e `PROMPT_CLAUDE.md` em uma pasta vazia.
3. Inicie o Claude Code nessa pasta e envie:

   ```text
   Leia README.md e PROMPT_CLAUDE.md. Crie todo o projeto especificado,
   valide-o sem acessar a API e apresente os comandos finais de uso.
   ```

4. Configure o `.env` e execute o projeto da mesma maneira descrita acima.

Em todos os fluxos, nunca envie uma chave real no prompt nem permita que o
arquivo `.env` seja versionado. A chave só deve ser adicionada depois que o
agente concluir a implementação e as verificações locais.

## Preparação

Requer Python 3.13 e o gerenciador de pacotes `uv`.

```bash
uv sync
```

Crie um `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sua_chave_aqui
```

O `.env` já deve estar listado no `.gitignore`. A chave também pode ser
fornecida diretamente pela variável de ambiente `OPENAI_API_KEY`.

## Execução

```bash
uv run python main.py
```

O programa deve exibir `Output do Agente:` seguido de um provérbio criado pelo
modelo. O texto exato varia entre as execuções.
