.PHONY: install start migrate seed generate
# Declara que os alvos listados (install, start, migrate, seed, generate) 
# são "phony", ou seja, não representam arquivos, mas sim comandos a serem executados.

install:
	uv sync
# Define o alvo "install". Quando você executa "make install", o comando "uv sync" 
# é executado para instalar ou atualizar as dependências do projeto com o uv.

start:
	uv run uvicorn src.main:app --reload
# Define o alvo "start". Executa a aplicação FastAPI com uvicorn em modo de recarga 
# automática (--reload) usando o uv.

migrate:
	uv run prisma migrate dev --name dev
# Define o alvo "migrate". Executa as migrações do Prisma para o ambiente de 
# desenvolvimento com o nome "dev".

seed:
	uv run python prisma/seed.py
# Define o alvo "seed". Executa o script seed.py para popular o banco de dados.

generate:
	uv run prisma generate
# Define o alvo "generate". Gera o cliente Prisma com base no schema.prisma.