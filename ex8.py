from functools import reduce

array =  ["casa", "python", "lambda"]

def soma_map_elementos(arr):
    mapeando = list(map(lambda element: len(element), arr))
    reduc = reduce(lambda acc, element: acc + element, mapeando, 0)
    return reduc, mapeando


reduced, mapped = soma_map_elementos(array) # desempacotamento >>>>>>>>>>

print(reduced)    
print(mapped)    