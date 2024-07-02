# Abstração
from pathlib import Path

log_file = Path(__file__).parent / 'log.txt'  # Indica que é para criar um aquivo com este nome, e salvar lá.
print(f'Caminho do arquivo: {log_file}')  # Retorna o caminho do arquivo, qual diretóierio esse arquivo está


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método Log')
    

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no arquivo de log')
        with open(log_file, 'a') as arquivo:  # open com 'a' ele adiciona linhas, com 'w' ele apaga e começa do 0
            arquivo.write(msg_formatada)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} {self.__class__.__name__}')


if __name__ == '__main__':
    l = LogPrintMixin()
    l.log_error('Mensagem qualquer')
    l.log_success('Eba, deu certo')

    l2 = LogFileMixin()
    l2.log_error('teste mixin')
    l2.log_success('uhuul')

