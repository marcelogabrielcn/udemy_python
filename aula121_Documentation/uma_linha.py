"""
Documentação do módulo 
Aqui vem o __name__, que deve ser o nome do módulo e título, algo assim

Se eu pular uma linha, e adicionar texto, aqui será a descrição que irá aparecer no help()
Independente de quantas linhas tiver, irá aparecer aqui como descrição
"""


print('Oii')
var_qualquer = 'nada'

def func_qualquer():
    """
    Aqui dentro da função, eu posso ter uma documentação também
    """
    ...


def soma(x: int | float, y: int | float) -> int | float:
    return x + y