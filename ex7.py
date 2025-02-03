array = [1, -2, 0, 3, -5, 0]


agrupar_numeros = (lambda arr: {'positivos': list(filter(lambda x: x > 0, arr)), 'negativos': list(
    filter(lambda x: x < 0, arr)), 'zeros': list(filter(lambda x: x == 0, arr))})


print(agrupar_numeros(array))
