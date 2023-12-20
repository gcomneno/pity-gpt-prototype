# Usa un'immagine di Python come base
FROM python:3.8

# Imposta la directory di lavoro
WORKDIR /app

# Copia il codice dell'applicazione nella directory di lavoro
COPY . /app

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Comando di avvio dell'app
CMD ["python", "app.py"]
