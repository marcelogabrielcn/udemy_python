pessoa = {
    'nome': 'Julia',
    'sobrenome': 'Nascimento',
}

(a1, a2), b = pessoa.items()

#print(a1, a2)
#print(b)
mais_dados_pessoa = {
    'altura': 1.82,
    'peso': 75,
}

pessoa_todos_dados = {**pessoa, **mais_dados_pessoa, 'mais_qlq': 9318}
print(pessoa_todos_dados)


def exibir_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados: ', args)  # Todos argumentos que vierem

    for chave, valor in kwargs.items():  # Todos argumentos nomeados (dicionários) que vierem
        print(chave, valor)


exibir_argumentos_nomeados(1, 2, **pessoa_todos_dados)
