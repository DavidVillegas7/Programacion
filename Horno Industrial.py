while True:
    temperatura_str = input()
    if temperatura_str == "FIN":
        break

    if not temperatura_str or temperatura_str == ".":
        print("Error")
        continue

    es_valido = True
    puntos = 0

    for caracter in temperatura_str:
        if caracter == ".":
            puntos += 1
            if puntos > 1:
                es_valido = False
                break
        elif not caracter.isdigit():
            es_valido = False
            break

    if not es_valido:
        print("Error")
        continue

    temperatura = float(temperatura_str)

    if temperatura < 100.0 or temperatura > 500.0:
        print("¡ADVERTENCIA! Temperatura fuera de rango")