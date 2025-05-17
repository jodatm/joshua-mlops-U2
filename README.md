Predicción de enfermedades usando GitHub + GitHub Actions

En el contexto médico actual, existe una abundancia de información sobre pacientes con enfermedades comunes. Sin embargo, las llamadas enfermedades huérfanas (raras o poco comunes) carecen de suficientes datos clínicos. Esto representa un reto para la predicción y diagnóstico temprano basado en síntomas.

El objetivo es construir un modelo capaz de predecir si un paciente puede estar sufriendo alguna enfermedad a partir de sus síntomas.

Estructura del Repositorio

```plaintext
raiz del repositorio/
│
├── DescripcionPipeline.md         # Explicación general del pipeline MLOps propuesto
├── Diagrama1.1.png                # Diagrama del flujo del pipeline (imagen PNG)
├── Diagrama1.svg                  # Versión vectorial del diagrama del pipeline
│
├── Dockerfile                     # Imagen Docker que contiene el servicio
├── app.py                         # Servicio Flask que expone la API de predicción
├── predictor.py                   # Función que simula el modelo de predicción
├── dependencias.txt               # Lista de dependencias necesarias en python
│
├── postman.png                    # Ejemplo de uso de la API con Postman
└── README.md                      # Instrucciones de uso y documentación general
│
└── tests/                         # Carpeta con pruebas del servicio
    ├── test_reportes.py           # Pruebas del modulo de reportes
    └── test_predictor.py          # Pruebas unitarias
```


Estados de Salud Retornados por el Modelo

La función simulada es capaz de retornar uno de los siguientes estados según los datos de entrada:

    NO ENFERMO
    ENFERMEDAD LEVE
    ENFERMEDAD AGUDA
    ENFERMEDAD CRÓNICA

Para ver los actions:
```python
https://github.com/jodatm/joshua-mlops-U2/packages
```

Para descargar y probar la imagen de docker:
```python
docker pull ghcr.io/jodatm/predictor-enfermedades:latest
```