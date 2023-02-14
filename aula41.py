# Operação ternária (condicional de uma linha)
print('Informação' if True else 'Outra informação')

# Bastante utilizado em verificação pequenas, por exemplo dígito do CPF
soma_digito = 10
novo_digito = soma_digito if soma_digito <= 9 else 0
print(novo_digito)

novo_digito2 = 0 if soma_digito > 9 else soma_digito
print(novo_digito2)
