from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data')
def get_data():
    # Solo devuelve un simple JSON
    return jsonify(message="¡Hola desde el backend-data!", source="Servicio Backend")

if __name__ == '__main__':
    # Corre en el puerto 5001 DENTRO del contenedor
    app.run(host='0.0.0.0', port=5001)