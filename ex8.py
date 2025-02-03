from functools import reduce


arr =  ["casa", "python", "lambda"]

mapeando = list(map(lambda element: len(element), arr))

print(mapeando)

reduc = reduce(lambda acc, element: acc + element, mapeando, 0)

print(reduc)