# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Creamos un directorio de trabajo
WORKDIR /app

# Copiamos los requisitos primero
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código de la app
COPY app.py .

# El comando para correr la app
CMD ["python", "app.py"]