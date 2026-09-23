# --- Imagem base ---
FROM python:3.12-slim

# Evita .pyc e força stdout/stderr sem buffer (logs aparecem na hora)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copia só o requirements primeiro para aproveitar cache de camadas do Docker:
# se o código mudar mas as dependências não, essa camada não é reconstruída.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Agora copia o restante do código
COPY . .

EXPOSE 5000

CMD ["python", "run.py"]