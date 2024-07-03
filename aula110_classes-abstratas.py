# Métodos abstratos, devem ser implementados nas subclasse, obrigatório
# Tem essas duas formas de criar uma classe abstrata, vamos usar a primeira

from abc import ABC, ABCMeta, abstractmethod

class Log(ABC):
    @abstractmethod  #Agora minha classe é abstrata, ou seja, log não pode ser usado diretamente
    def _log(self, msg): ...  # Não vai ter corpo, pois será abstrato
        
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} {self.__class__.__name__}')


#class Log2(metaclass=ABCMeta):  # Segunda forma de criar classe abstrata
#    ...

#l = Log()  # Se tentar executar, vai ter erro, pois é uma classe abstrata
# Para usar essa clase, devo herdar em outra clase e implementar o método que quero usar, com a mesma assinatura

l = LogPrintMixin()
l.log_error('Oii')

#Para uma classe ser abstrata em python, ela precisar herdar de ABC, e ter ao menos algum método abstrato