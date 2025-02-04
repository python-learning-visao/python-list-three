array = [1, -2, 0, 3, -5, 0]

def agrupar_numeros(arr):
    positivos = list(filter(lambda x: x > 0, arr))
    negativos = list(filter(lambda x: x < 0, arr))
    zeros = list(filter(lambda x: x == 0, arr))
    return {'positivos': positivos, 'negativos': negativos, 'zeros': zeros}

print(agrupar_numeros(array))