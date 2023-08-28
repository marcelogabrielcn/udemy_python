# Criar uma lista de tarefas, onde o usuário pode criar uma tarefa ou listar. Pode desfazer o ultimo comando ou refazer o que havia desfeito

lista_de_tarefas = []
app = True

while app == True:
    acao_usuario = input(str('Comandos: listar, desfazer, refazer, sair. \nDigite uma tarefa ou comando: '))
    if acao_usuario == 'listar':
        for tarefas in lista_de_tarefas:
            print(tarefas)
    elif acao_usuario == 'desfazer':
        ...
    elif acao_usuario == 'refazer':
        ...
    elif acao_usuario == 'sair':
        app = False
    else:
        lista_de_tarefas.append(acao_usuario)
        for tarefas in lista_de_tarefas:    
            print(tarefas)

print('Obrigado por utlizar o Tarefy. Volte sempre!❤️')

