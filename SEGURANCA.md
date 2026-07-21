# FORMAS SEGURAS DE SALVAR API KEY

> A forma mais segura de manter a chave fora do repositório e ainda deixar o projeto funcionando: A forma mais segura é guardar a chave em uma variável de ambiente no próprio terminal ou em um arquivo local que não seja versionado.

## Opção 1: definir a variável no terminal
No Linux/macOS:

```bash
export OPENAI_API_KEY="sua_chave_aqui"
```

No Windows PowerShell:

```powershell
$env:OPENAI_API_KEY="sua_chave_aqui"
```

Assim, o código consegue ler a variável sem precisar do arquivo .env.

A variável é apagada quando:
- você fecha o terminal
- abre outro terminal novo
- reinicia o computador
- inicia uma nova sessão de shell

Opção 2: usar um arquivo .env local, mas ignorá-lo no Git
Crie um arquivo .env na raiz do projeto:

```env
OPENAI_API_KEY=sua_chave_aqui
```

Depois adicione isso no seu .gitignore se existir:

```gitignore
.env
```

Se não existir, crie o arquivo .gitignore com essa linha.

Opção 3: usar um gerenciador de segredos
Se for para uso mais sério, você pode usar:
- Docker secrets
- GitHub Secrets
- Azure Key Vault
- AWS Secrets Manager

Recomendação prática para seu caso:
- use .env localmente
- adicione .env ao .gitignore
- nunca mande esse arquivo para o Git

Importante:
- o seu settings.py já está preparado para ler .env
- então, se a chave estiver em uma variável de ambiente, também funciona dependendo do ambiente

Se quiser, eu posso te ajudar a ajustar o projeto para aceitar a chave tanto de .env quanto de variável de ambiente.