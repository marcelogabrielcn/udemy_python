# nomes = ['Lucas', 'João', 'Kevin']
# nome1, nome2, nome3 = nomes

nome1, nome2, nome3 = ['Lucas', 'João', 'Kevin']  # É a mesma coisa de cima.
# Se tiver mais variáveis ou mais valores, vai dar erro, tem que ser quantidades iguais.

print(nome2)


nome4, *restante = ['José', 'Maria', 'Juca', 'Zeka']  # * Cria uma lista que salva os demais values.

print(nome4)
print(restante)  # Restantes é uma lista 

nome4, *_ = ['José', 'Maria', 'Juca', 'Zeka']  
# Em python é comum usar "_" para restos que não serão utilizados

print(nome4, _)
