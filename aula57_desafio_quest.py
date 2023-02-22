# Challenge 

questionario = [
    {
        'Pergunta': 'Quando é 5 x 5?',
        'Opções': ['10', '15', '25', '50'],
        'Resposta': '25'
    },
    {
        'Pergunta': 'Qual a raiz quadrada de 81?',
        'Opções': ['08', '09', '10', '11'],
        'Resposta': '09'
    },
    {
        'Pergunta': 'Quanto é 36 / 12?',
        'Opções': ['03', '06', '07', '09'],
        'Resposta': '03'
    }
]

acertos = 0

for questoes in questionario:
    print(questoes['Pergunta'])
    print(f'\nOpções:')
    contador_temp = 1

    for opcoes in questoes['Opções']:
        print(f'{contador_temp}) {opcoes}')
        contador_temp += 1

    contador_temp = 1
    entrada_resposta = input(('Escolha uma opção: '))
    resposta = questoes['Opções'][int(entrada_resposta) - 1]
    
    if resposta == questoes['Resposta']:
        acertos += 1  
        print('Acertou ✔')
    else:
        print('Errou ❌')
    print()
    
print(f'Você acertou {acertos} de {len(questionario)} perguntas')
