lista = ['Marcelo', 23, 1.82, True, (34, 53), {'Dicionário':'teste'}]

for item in lista:
    if isinstance(item, str):
        print('Aqui temos uma String: ', item)
    elif isinstance(item, int):
        print('Aqui temos um valor inteiro: ', item)
    elif isinstance(item, float):
        print('Aqui temos um valor de num. flutuante: ', item)
    elif isinstance(item, bool):
        print('Aqui temos um valor binário: ', item)
    elif isinstance(item, dict):
        print('Aqui temos um dicionário: ', item)
    elif isinstance(item, tuple):
        print('Aqui temos uma tupla: ', item)
    else:
        print('Não sei que tipo é isso: ', item)

