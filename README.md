# Crie o ambiente virtual (se ainda não existir)
python3 -m venv .venv

# Ative o ambiente virtual
source .venv/bin/activate

# Instale as dependências do requirements.txt
pip install --upgrade pip
pip install -r requirements.txt


## Via docker

### Construir imagem
```bash
docker build -t airpocalypse-backend .
```

### Executar
```bash
docker run --rm -it -p 8080:8080 airpocalypse-backend
```

