class MeuError(Exception): 
    ...
    

class OutroError(Exception): ...

def levantarException():
    exception_ = MeuError('A mensagem de erro vem aqui')  # Esse raie vai levantar um erro, e mostrar a mensagem ao usuário
    exception_.add_note('Aqui posso adicionar uma nota e explicar o erro')
    raise exception_


try:
    levantarException()
except (MeuError, ZeroDivisionError) as error:  # Se algum tipo e exceção que estiver aqui em except ocorrer durante o code, vai entrar nessa clausula
    print(error.__class__.__name__)
    print()
    exception_ = OutroError('Será lançado de novo o erro')
    raise exception_ from error
