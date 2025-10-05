FROM python:3.11-slim

WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia todo o código
COPY . .

# Expõe a porta
EXPOSE 8080

# Comando padrão roda a main apenas:
CMD ["python", "-u", "src/main.py", "--log-level", "debug"]