from flask import Flask, jsonify
import requests
import redis
import os

app = Flask(__name__)

# Conectamos a Redis usando su nombre de servicio 'db-cache'
# Docker Compose hace que 'db-cache' se resuelva a la IP correcta.
cache = redis.StrictRedis(host='db-cache', port=6379, db=0, decode_responses=True)

@app.route('/')
def get_combined_data():
    
    # 1. Intentar obtener el dato desde el caché (Redis)
    cached_message = cache.get('backend_message')
    
    if cached_message:
        return jsonify(
            message=cached_message,
            source="Caché de Redis"
        )
    
    # 2. Si no está en caché, llamar al servicio 'backend-data'
    # Usamos el nombre del servicio 'backend-data' y su puerto interno 5001
    try:
        response = requests.get('http://backend-data:5001/data')
        data = response.json()
        message = data['message']
        
        # 3. Guardar en caché para la próxima vez
        cache.set('backend_message', message)
        
        return jsonify(
            message=message,
            source="Servicio Backend (obtenido ahora)"
        )
    
    except requests.ConnectionError:
        return jsonify(error="El servicio backend-data no está disponible"), 500

if __name__ == '__main__':
    # Corre en el puerto 5000 DENTRO del contenedor
    app.run(host='0.0.0.0', port=5000)