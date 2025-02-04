array =  [1, 2, 3, 4, 5, 6]
    
def separar_par_impar(arr):
    par = list(filter(lambda x: x % 2 == 0, arr))
    impar = list(filter(lambda x: x % 2 != 0, arr))
    return {'par': par, 'impar': impar}

print(separar_par_impar(array))
