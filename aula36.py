"""
Tuplas são parecidas com listas, porém são imutáveis, ou seja, 
Não são alteráveis!
São mais rápidas e simples de executar, tem ganho energético.
"""

tuplas = 'José', 'Maria', 'Juca', 'Zeka'
tupla2 = ()
# Uma tupla pode ser delcara apenas com valores, sem chaves, ou com parenteses.

print(tuplas)
print(type(tupla2))
print(tuplas[2])

lista = ['Lucas', 'João', 'Kevin']
tupla = tuple(lista)  # Também é possível converter os tipos entre tuplas e listas, vice-versa
