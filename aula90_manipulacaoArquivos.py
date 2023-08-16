caminho_arquivo = 'C:\\Users\\Gabriel\\Documents\\udemy_python2023\\'
caminho_arquivo += 'aulaXX2.txt'
with open(caminho_arquivo, 'w') as arquivo:
    ...
    #print('Hello World')
    #print('O arquivo será fechado depois daqui')

# Náo é necessário dar o close(), pois o with já abre e fecha o arquivo

#Para escrever no arquivo, usamos write:

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Minha primeira linha escrita.\n')
    arquivo.write('Minha segunda linha, lembrando da quebra de linha na anterior.\n')


with open(caminho_arquivo, 'r') as leitura:
    
    print(leitura.read())


with open(caminho_arquivo, 'a+') as escrita_leitura:
    escrita_leitura.write('Minha terceira linha escrita\n')
    escrita_leitura.seek(0,0)  # Move o "cursor" do python, que está fazendo a leitura para o topo do arquivo
    print(escrita_leitura.read())


with open(caminho_arquivo, 'a+') as arquivo:
    arquivo.writelines(
        ('Linha 4\n', 'Linha 5\n')
    )  # O Writelines serve para escrever várias linhas de uma só vez
    arquivo.seek(0,0)
    print(arquivo.read())

# Tem também o readline(), que vai lendo uma linha por vez, como se fosse o next() em iteráveis
# O modo 'w' apaga o arquivo e começa escrever de novo, já o modo 'a' da um append no final do arquivo.

with open(caminho_arquivo, 'a+', encoding='utf-8') as teste_utf:  
    # Se não tiver esse encoding, que é a formatação de textos do windows, ele salva em um formato que não tem pontuação
    teste_utf.write('Linha X, Atenção com a pontuação')
    teste_utf.seek(0,0)
    print(teste_utf.read())
