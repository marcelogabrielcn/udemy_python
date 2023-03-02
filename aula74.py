from aula74_packege.aula74_modulo_teste import somar_dentro_do_pacote
import aula74_packege.aula74_modulo_teste

num_1 = 20
num_2 = 10

soma = somar_dentro_do_pacote(num_1, num_2)   
print(soma)
soma_2 = aula74_packege.aula74_modulo_teste.somar_dentro_do_pacote(num_1, num_2)  #Gigante
print(soma_2)
