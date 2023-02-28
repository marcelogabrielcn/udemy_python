import sys  # Importante separar as importações padrão do python dos meus próprio módulos

import aula73_module  # Módulos que estão na mesma pasta que o arquivo principal

#print('Este módulo se chama: ', __name__)
#print(*sys.path, sep='\n')

num_1 = 4
num_2 = 9
soma = aula73_module.soma(num_1, num_2)  # Função que está la no módulo de outra aula
print(soma)
