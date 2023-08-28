# Criar uma lista de tarefas, onde o usuário pode criar uma tarefa ou listar. Pode desfazer o ultimo comando ou refazer o que havia desfeito

def listar(lista_de_tarefas):
    print()
    if not lista_de_tarefas:
        print('Não há nenhuma tarefa para listar.')
        return

    print('Tarefas:')
    for tarefa in lista_de_tarefas:
        print(f'\t{tarefa}')


def desfazer(lista_de_tarefas, tarefas_refazer):
    print()
    if not lista_de_tarefas:
        print('Não há nenhuma tarefa para desfazer.')
        return
    
    tarefa = lista_de_tarefas.pop()
    tarefas_refazer.append(tarefa)


def refazer(lista_de_tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Não há nenhuma tarefa para refazer.')
        return
    
    tarefa = tarefas_refazer.pop()
    lista_de_tarefas.append(tarefa)


def adicionar_tarefa(tarefa, lista_de_tarefas):
    print()
    if not tarefa:
        print('Ops, parece que você não digitou nenhuma tarefa.')
        return
    lista_de_tarefas.append(tarefa)
    listar(lista_de_tarefas)

lista_de_tarefas = []
tarefas_refazer = []

while True:
    acao_usuario = input(str('Comandos: listar, desfazer, refazer, sair. \nDigite uma tarefa ou comando: '))
    if acao_usuario == 'listar':
        listar(lista_de_tarefas)
    elif acao_usuario == 'desfazer':
        desfazer(lista_de_tarefas, tarefas_refazer)
    elif acao_usuario == 'refazer':
        refazer(lista_de_tarefas, tarefas_refazer)
    elif acao_usuario == 'sair':
        break
    else:
        adicionar_tarefa(acao_usuario.strip(), lista_de_tarefas)


print('Obrigado por utlizar o Tarefy. Volte sempre!❤️')

