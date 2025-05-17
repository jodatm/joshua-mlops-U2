import os
import json
import requests

API_URL = "http://localhost:5000"

def test_estadisticas_vacias():
    # Asegúrate que el archivo esté vacío al principio
    if os.path.exists("registro_predicciones.json"):
        os.remove("registro_predicciones.json")
    
    r = requests.get(f"{API_URL}/reporte")
    data = r.json()
    assert data['totales_por_categoria'] == {}

def test_todas_las_categorias():
    entradas = [
        (37, 5, 70),     # NO ENFERMO
        (38, 5, 80),     # ENFERMEDAD LEVE
        (39, 5, 50),    # ENFERMEDAD AGUDA
        (38.5, 7, 55),    # ENFERMEDAD CRÓNICA
        (40, 9, 150),   # ENFERMEDAD TERMINAL
    ]
    esperados = [
        "NO ENFERMO",
        "ENFERMEDAD LEVE",
        "ENFERMEDAD AGUDA",
        "ENFERMEDAD CRÓNICA",
        "ENFERMEDAD TERMINAL"
    ]

    for (fiebre, dolor, frecuencia), esperado in zip(entradas, esperados):
        r = requests.post(f"{API_URL}/predecir", json={
            "fiebre": fiebre,
            "dolor": dolor,
            "frecuencia_cardiaca": frecuencia
        })
        assert r.status_code == 200
        assert r.json()['resultado'] == esperado

    # Revisión de reporte
    r = requests.get(f"{API_URL}/reporte")
    data = r.json()

    for categoria in esperados:
        assert categoria in data['totales_por_categoria']
        assert data['totales_por_categoria'][categoria] >= 1

    assert data['ultimas_5_predicciones'][-1]['resultado'] == "ENFERMEDAD TERMINAL"
