def dobrar_elementos(arr: list) -> list:
    x = list(map(lambda x: x * 2, arr))
    
    return x

print(dobrar_elementos([1, 2, 3, 4, 5]))