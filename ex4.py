names = ["Ana", "Lucas", "Fernanda", "João"] 

def filter_names(arr: list) -> list:
    x  = list(filter(lambda element: len(element) > 5, arr))
    
    return x

print(filter_names(names))