from functools import reduce
# obj passado pelo professor
alunos = { 
"João": [8, 7, 9, 2],  # (notas: 8, 7, 9; peso: 2) 
"Ana": [5, 6, 7, 3]    
# (notas: 5, 6, 7; peso: 3) 
} 

def media_ponderada(alunos):
    resultado = {}
    for aluno, valores in alunos.items():
        peso = valores[-1]
        notas = valores[:-1]
        media_ponderada = reduce(lambda acc, nota: acc + nota * peso, notas, 0)
        total_pesos = len(notas) * peso
        media = media_ponderada / total_pesos
        resultado[aluno] = f'{media:.0f}' # ou round(media, 2) que acho mais clean
    
    return resultado

print(media_ponderada(alunos))