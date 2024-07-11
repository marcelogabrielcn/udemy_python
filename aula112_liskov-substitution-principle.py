from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, msg) -> None:  # Essa seta diz qual deve ser o tipo de retorno da função, para outros devs verem
        self.msg = msg

    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail enviando: ', self.msg)
        return True


class NotificacaoSms(Notificacao):
    def enviar(self) -> bool:
        print('SMS enviando: ', self.msg)
        return False



def notificar(notificacao: str):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print("A notificação foi enviada")
    else:
        print("A notificação não foi enviada")
        

#n1 = NotificacaoEmail('Test notification')
#n1.enviar()

notificar(NotificacaoEmail("Testando e-mail"))
notificar(NotificacaoSms("Testando SMS"))
