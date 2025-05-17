from flask import Flask, request, jsonify
from predictor import predecir_estado

app = Flask(__name__)

@app.route('/predecir', methods=['POST'])
def predecir():
    data = request.get_json()
    fiebre = data.get('fiebre')
    dolor = data.get('dolor')
    frecuencia = data.get('frecuencia_cardiaca')

    if None in [fiebre, dolor, frecuencia]:
        return jsonify({'error': 'Todos los valores deben estar'}), 400

    resultado = predecir_estado(fiebre, dolor, frecuencia)
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
