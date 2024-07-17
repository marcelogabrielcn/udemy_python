class MeuError(Exception): 
    ...


def levantarException():
    raise MeuError('A mensagem de erro vem aqui')  # Esse raie vai levantar um erro, e mostrar a mensagem ao usuário


levantarException()


