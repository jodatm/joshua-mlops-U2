graph TD
    A[Recopilación de datos] --> B[Limpieza y preprocesamiento]
    B --> C[Análisis exploratorio de datos]
    C --> D["División de datos(Train y Test)"]
    D --> E["Selección del modelo"]
    E --> F[Selección de características]
    F --> G[Entrenamiento de modelos]
    G --> H[Validación y prueba del modelo]
    H --> I[Despliegue en producción]
    I --> J[Monitoreo en producción]
    J --> K[Nuevos datos para re-entrenamiento]

    A -->|Datos médicos| B
    B -->|Datos limpios| C
    D -->|Datos de entrenamiento| F
    D -->|Datos de prueba| G
    H -->|Modelo en producción| I
