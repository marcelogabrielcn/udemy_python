from log import LogFileMixin, LogPrintMixin


l = LogPrintMixin()
l.log_error('Mensagem qualquer')
l.log_success('Eba, deu certo')

l2 = LogFileMixin()
l2.log_error('Adicionando linhas com log')
l2.log_success('adicionando linhas, success')
