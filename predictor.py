def predecir_estado(fiebre, dolor, frecuencia_cardiaca):
    alteraciones = 0
    terminal = False

    # Evaluar fiebre severa
    if fiebre >= 39.5:
        terminal = True
    elif fiebre >= 38:
        alteraciones += 1

    # Escala de dolor muy alta
    if dolor >= 9:
        terminal = True
    elif dolor >= 6:
        alteraciones += 1

    # Frecuencia cardiaca muy fuera de rango
    if frecuencia_cardiaca < 40 or frecuencia_cardiaca > 140:
        terminal = True
    elif frecuencia_cardiaca < 60 or frecuencia_cardiaca > 100:
        alteraciones += 1
    
    if terminal:
        return "ENFERMEDAD TERMINAL"
    elif alteraciones == 0:
        return "NO ENFERMO"
    elif alteraciones == 1:
        return "ENFERMEDAD LEVE"
    elif alteraciones == 2:
        return "ENFERMEDAD AGUDA"
    else:
        return "ENFERMEDAD CRÓNICA"
