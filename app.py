from flask import Flask, request, jsonify
from predictor import predecir_estado
import json
import os
from datetime import datetime

app = Flask(__name__)
registro_file = 'registro_predicciones.json'

def guardar_prediccion(prediccion):
    data = []
    
    if os.path.exists(registro_file):
        with open(registro_file, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    
    data.append(prediccion)
    with open(registro_file, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/predecir', methods=['POST'])
def predecir():
    data = request.get_json()
    fiebre = data.get('fiebre')
    dolor = data.get('dolor')
    frecuencia = data.get('frecuencia_cardiaca')

    if None in [fiebre, dolor, frecuencia]:
        return jsonify({'error': 'Todos los valores deben estar'}), 400

    resultado = predecir_estado(fiebre, dolor, frecuencia)
    prediccion = {
        'fecha': datetime.now().isoformat(),
        'fiebre': fiebre,
        'dolor': dolor,
        'frecuencia_cardiaca': frecuencia,
        'resultado': resultado
    }
    guardar_prediccion(prediccion)
    return jsonify({'resultado': resultado})

@app.route('/reporte', methods=['GET'])
def reporte():
    if not os.path.exists(registro_file):
        return jsonify({'mensaje': 'no hay predicciones registradas.'}), 200

    with open(registro_file, 'r') as f:
        try:
            datos = json.load(f)
        except json.JSONDecodeError:
            return jsonify({'error': 'Error al leer el archivo.'}), 500

    # Totales por categoría
    conteo = {}
    for entrada in datos:
        categoria = entrada['resultado']
        conteo[categoria] = conteo.get(categoria, 0) + 1

    # Últimas 5 predicciones
    ultimas_predicciones = datos[-5:]

    # Última fecha
    ultima_fecha = datos[-1]['fecha'] if datos else None

    return jsonify({
        'totales_por_categoria': conteo,
        'ultimas_5_predicciones': ultimas_predicciones,
        'fecha_ultima_prediccion': ultima_fecha
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
