try:
    a = 27
    b = 0
    c = a / b
    print(c)
except ZeroDivisionError:  # Trata especificamente o erro de divisão por zero
    print('Ops, divisão por zero não é possível.')

except NameError:  # Trata especificamente o erro de nome das variáveis, ou quando não estão definidas
    print('Alguma variável não está definida.')

except Exception:  # Trata todas as exceções, "Exception" é a classe suprema de erros
    print('Erro desconhecido.')

print('Fim do programa')
