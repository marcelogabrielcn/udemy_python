#with open('file116.txt', 'w') as arquivo:
 #   ...


class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None


    def __enter__(self):
        print('Abrindo arquivo')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo


    def __exit__(self, class_exception, exception_, traceback_):
        print('Fechando arquivo')
        self._arquivo.close()

        #raise class_exception('Minha mensagem de Exceção')  # Assim eu posso levantar minha exceção, porém, o raise anula o ruturn

        print(class_exception)
        print(exception_)
        print(traceback_)

        return True  # Jã tratei o erro de alguma forma, dessa maneira o erro apenas irá passar.


with MyOpen('aula116.txt', 'w', ) as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('With??', arquivo)  # Dentro do alguma_coisa, vai estar o return que colocamos no enter.