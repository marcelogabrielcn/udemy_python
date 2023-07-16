# Group By - Ordenar por
from itertools import groupby


alunos_notas = [
    {'nome': 'Yuri', 'nota': 'C'},
    {'nome': 'Juliana', 'nota': 'B'},
    {'nome': 'Karina', 'nota': 'A'},
    {'nome': 'Yolanda', 'nota': 'B'},
    {'nome': 'Erika', 'nota': 'A'},
    {'nome': 'Vitor', 'nota': 'A'},
    {'nome': 'Bartolomeu', 'nota': 'A'},
    {'nome': 'Sabrina', 'nota': 'B'},
    {'nome': 'Tatiana', 'nota': 'B'},
    {'nome': 'Stefany', 'nota': 'C'},
    {'nome': 'Jhoe', 'nota': 'C'},
]


def ordena(x):
    return x['nota']


alunos = ['a', 'a', 'a', 'a', 'a', 'b', 'c', 'a']
grupos_teste = groupby(sorted(alunos))  #Gera também um iterável, 2. Precisa do sorted, porque ele só ordena os dados em sequencia, se tiver um outro a no fim da lista, ele cria outro grupo

#for chave, grupo in grupos_test:
    #print(chave)
    #print(list(grupo))

alunos_agrupados = sorted(alunos_notas, key=ordena)  # Recebe a lista que contém os dicionários para serem ordenados, e recebe uma função que recebe aluno e retorna aluno[nota]
grupos = groupby(alunos_agrupados, key=ordena)  #Quero ordenar por notas, estão passo uma função lambda que me retorna as notas

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)
    print()
