
class BancoDelas:
    def __init__(self):
        self._clientes = []

    @property
    def clientes(self):
        return self._clientes

    @clientes.setter
    def clientes(self, cliente):
        self._clientes.append(cliente)


class Cliente:
    def __init__(self, nome, telefone, renda, CC):
        self.nome = nome
        self.telefone = telefone
        self.renda = renda
        self.conta_corrente = CC
        CC.adicionar_titular(self)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def renda(self):
        return self.__renda

    @renda.setter
    def renda(self, renda):
        self.__renda = renda

    def __str__(self):
        return f'{self.nome}'


class ContaCorrente:
    def __init__(self):
        self.__saldo = 0.0
        self._titulares = []

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, deposito):
        self.__saldo += deposito

    def sacar(self, saque):
        self.__saldo -= saque

    def adicionar_titular(self, titular):
        self._titulares.append(titular)

    def __str__(self):
        lista = str([str(pe) for pe in self._titulares])
        return 'Esta conta possui os seguintes titulares:'+lista


conta = ContaCorrente()
pessoa = Cliente('Juliana', '83991828383', 100, conta)
pessoa2 = Cliente('Sandra', '989123145454', 5000, conta)
print(conta)
pessoa.conta_corrente.depositar(100)
print(pessoa2.conta_corrente.saldo)
# Atores: BancoDelas, ContaCorrente, Cliente
# Propriedades: BancoDelas - Clientes
#               Cliente - Nome, Telefone e renda
#               ContaCorrente - saldo
# Métodos: BancoDelas - Add e remover clientes
#          Cliente -
