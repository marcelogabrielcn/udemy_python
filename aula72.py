import sys  # Importar módulo inteiro
from sys import exit  # Importando um método específico
import random as aleatorio  # Importa com um apelido, deixando o nome livre para outro uso
from random import *  # Má prática, pois importa tudo, sem eu saber o que vem, podendo sobrescrever

print(sys.platform)  # Trás o kernel do sistema
print(aleatorio.randint(0, 9))  # Trás um num aleatório entre 0 e 9
