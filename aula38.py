import os


lista_de_compras = []
opcoes = 'IALS'

while True:
    entrada_user = input('Digite (I)nserir, (A)pagar, (L)istar ou (S)air: ').upper()
    if entrada_user not in opcoes:
        print('Ops, não entendi, digite (I, A ou L)')
        continue

    if entrada_user == 'I':
        inserir_item = input('Digite qual item deseja inserir: ')
        lista_de_compras.append(inserir_item)
        os.system('cls')

    if entrada_user == 'L':
        if not lista_de_compras:
            print('Ops, a lista está vazia.')
            os.system('cls')
            continue
        os.system('cls')
        for indice, produto in enumerate(lista_de_compras):
            print(indice, produto)

    if entrada_user == 'A':
        if not lista_de_compras:
            print('Ops, a lista está vazia.')
            os.system('cls')
            continue
        try:
            qual_apagar = input('Digite o número do produto que deseja remover: ')
            qual_apagar = int(qual_apagar)
            del lista_de_compras[qual_apagar]
            os.system('cls')
        except:
            print('Não entendi...')
            continue

    if entrada_user == 'S':
        print('Até logo...')
        break

print('Fim do programa.')
