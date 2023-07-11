import random

def generateData():
    # Generar una lista de 2000 elementos aleatorios
    lista_elementos = [random.randint(1, 1000) for _ in range(2000)]
    return lista_elementos

