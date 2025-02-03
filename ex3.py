from  functools import reduce

def somando_elementos(arr: list) -> int:
    x = reduce(lambda acc, element: acc + element, arr, 0)  
    return x

lista = [1,2,3,4,5]
print(somando_elementos(lista))