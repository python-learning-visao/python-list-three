lista =  [1, 2, 3, 4, 5, 6]

separar_par_impar = lambda arr: {
    'par': list(filter(lambda x: x % 2 == 0, arr)), 
    'impar': list(filter(lambda x: x % 2 != 0, arr))
}

print(separar_par_impar(lista))
    