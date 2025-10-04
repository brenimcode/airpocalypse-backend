# airpocalypse-backend

Este repositório contém o backend do projeto Airpocalypse, uma API construída com FastAPI.

O README abaixo descreve tudo que é necessário para configurar, executar e desenvolver localmente este projeto.

## Pré-requisitos

- Python 3.10+ (ou 3.9 — porém 3.10+ recomendado)
- Git
- pip
- Recomenda-se usar um virtual environment (venv / virtualenv / conda)

## Dependências

Para instalar as dependências (recomendado dentro de um virtualenv):

```bash
# criar e ativar um virtualenv (Linux/macOS)
python3 -m venv .venv
source .venv/bin/activate

# atualizar pip
pip install --upgrade pip

# instalar dependências
pip install -r requirements.txt
```

# Executar a main

```bash
python3 src/main.py
```

Depois de iniciar, a API estará disponível em `http://0.0.0.0:8000/` (ou `http://localhost:8000/`).

### Documentação automática (Swagger)

Após iniciar o servidor, a documentação interativa estará disponível em:

- Swagger UI: `http://localhost:8000/docs`


## Banco de Dados com Docker Compose

O projeto já inclui um serviço Postgres pronto para uso via Docker Compose.

### Subindo o banco de dados

1. Certifique-se de que Docker e Docker Compose estão instalados.
2. No terminal, navegue até a pasta do projeto onde está o arquivo `docker-compose.yml` que é uma antes de SRC.
3. Execute o comando abaixo para subir apenas o banco:

```bash
docker-compose up
```

O banco estará disponível em:
- Host: `localhost`
- Porta: `5433`
- Usuário: `postgres`
- Senha: `123`
- Banco: `postgres`

Essas credenciais estão definidas no `docker-compose.yml` e podem ser alteradas conforme sua necessidade.

### Parando o banco

Para parar o banco:
```bash
docker-compose down
```

### Para criar a tabela INSCRITOS usando um script, execute o comando abaixo:
```bash
python3 src/create_tables.py
```
