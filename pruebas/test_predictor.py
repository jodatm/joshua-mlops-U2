import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from predictor import predecir_estado

def test_enfermedad_leve():
    resultado = predecir_estado(38, 5, 80)
    assert resultado == "ENFERMEDAD LEVE"

def test_enfermedad_terminal():
    resultado = predecir_estado(40, 9, 150)
    assert resultado == "ENFERMEDAD TERMINAL"

def test_no_enfermo():
    resultado = predecir_estado(37, 5, 70)
    assert resultado == "NO ENFERMO"

def test_enfermedad_aguda():
    resultado = predecir_estado(39, 5, 50)
    assert resultado == "ENFERMEDAD AGUDA"

def test_enfermedad_cronica():
    resultado = predecir_estado(38.5, 7, 55)
    assert resultado == "ENFERMEDAD CRÓNICA"
