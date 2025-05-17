FROM python:3.9-slim

WORKDIR /app

COPY dependencias.txt .
RUN pip install --no-cache-dir -r dependencias.txt

COPY . .

# Puse este porque el enunciado lo sugeria
EXPOSE 5000

CMD ["python", "app.py"]
