import re


cpf = input('Digite o CPF: ')
cpf_formatado = re.sub(r'[^0-9]', '', cpf)

print(cpf)
print(cpf_formatado)
