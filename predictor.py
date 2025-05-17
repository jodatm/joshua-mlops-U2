def predecir_estado(fiebre, dolor, frecuencia_cardiaca):
    alteraciones = 0

    # Fiebre
    if fiebre >= 38:
        alteraciones += 1

    # Escala de dolor
    if dolor >= 6:
        alteraciones += 1

    # Frecuencia cardiaca
    # Fuente: https://medlineplus.gov/spanish/ency/article/003081.htm
    if frecuencia_cardiaca < 60 or frecuencia_cardiaca > 100:
        alteraciones += 1

    if alteraciones == 0:
        return "NO ENFERMO"
    elif alteraciones == 1:
        return "ENFERMEDAD LEVE"
    elif alteraciones == 2:
        return "ENFERMEDAD AGUDA"
    else:
        return "ENFERMEDAD CRÓNICA"
