class Error(Exception):
    pass
class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break
    except ValueError:
        print('Valor inválido. Por favor, digite um número')
    except InputError as ex:
        print(ex)

'''
lista = [1, 10]
try:
    div = 10 / 1
    num = lista[1]
    x = a
except ZeroDivisionError:
    print('Não é possível realizar divisão por zero')
except IndexError:
    print('Erro ao acessar lista')
except BaseException as ex:
    print(f'Erro desconhecido: {ex}')
'''
