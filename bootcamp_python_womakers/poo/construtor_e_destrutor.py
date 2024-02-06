# construtores e destrutores

class MinhaClasse:
    def __init__(self, nome):
        self.nome = nome
        print('MinhaClasse chamou o construtor padrão!')

    def __del__(self):
        print(f'MinhaClasse chamou o destrutor de {self.nome}')


class MinhaClasse2:
    pass


class MinhaClasse3:
    def __init__(self, param):
        print(
            f'MinhaClasse3: chamou o construtor padrão com o parametro {param}')


print('Começou a execução do programa')
objeto1 = MinhaClasse('Bambi')
del objeto1  # como chamei explicitamente antes da finalização da execução do programa,
# ele chamou o destrutor aqui.
print('Vai terminar a execução do programa')
exit()  # chamou o destrutor da classe
# já é chamada automaticamente pelo interpretador.
# Chamado quando o programa se encerra e a coleta de lixo acontece

objeto2 = MinhaClasse2()
objeto3 = MinhaClasse3(123)
