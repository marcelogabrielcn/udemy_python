try:
    variavel = 'Marcelo Gabriel'

    print(variavel[892])  # Vai dar um erro: IndexError
except IndexError as error:  # O as é um apelido, pode ser qualquer palavra no lugar de error (porém é mais comum)
    print('Houve um erro: ', error)  # Saída: 'Houve um erro:  string index out of range'
    print('Nome do erro: ', error.__class__.__name__)  # Retorna o nome do erro certinho
else:  # Usado caso não tenha exceptions
    print('Não corrreu nenhum erro.')
finally:
    print('Finalmente executarei este bloco')  # Vai ser executado independente da exceção.

