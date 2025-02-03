arr = [3, 1, 4, 2]

def elevar_ordenar(arr: list) -> list:
    elevar = list(map(lambda x: x**2, arr))
    
    ordenar = sorted(elevar)
    
    return ordenar, elevar

ordenar, elevar = elevar_ordenar(arr)

print(elevar)
print(ordenar)