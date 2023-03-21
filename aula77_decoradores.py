def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Antes da decoração...')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O resultado foi: {resultado}')
        print('Pronto, foi decorado')
        return resultado
    return interna


@criar_funcao
def inverte_string(string):
    return(string[::-1])


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Parâmetro deve ser uma string')


#inverte_string_checando_parametro = criar_funcao(inverte_string)
#invertida = inverte_string_checando_parametro("Marcelo")
#print(invertida)

invertida = inverte_string('Marcelo')
print(invertida)
