tup =  [(2, 8), (4, 5, 6), (1, 2)]

# Função lambda para verificar se a média da tupla é igual a um valor 'alvo'
verifica_media = lambda tupla, alvo: sum(tupla) / len(tupla) == alvo if len(tupla) > 0 else False

# Definir a média desejada (exemplo: média 5)
media_alvo = 5

# Filtrar as tuplas que têm média igual a 'media_alvo'
resultado = list(filter(lambda tupla: verifica_media(tupla, media_alvo), tup))

print(resultado)