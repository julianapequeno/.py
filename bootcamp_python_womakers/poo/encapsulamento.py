class Quadrado:
    def __init__(self, medida):
        self.altura = medida
        self.largura = medida

    @property  # decorator
    def altura(self):
        return self.__medida

    @altura.setter
    def altura(self, valor):
        if valor < 0:
            raise ValueError()
        self.__medida = valor

    @property
    def largura(self):
        return self.__medida

    @largura.setter
    def largura(self, valor):
        if valor < 0:
            raise ValueError()
        self.__medida = valor

    def area(self):
        return self.largura * self.altura

    def __str__(self):
        return f'Sou um quadrado com {self.altura} de altura e {self.largura} de largura'


quadrado = Quadrado(4)
try:
    quadrado.altura = -122
    quadrado.altura = 8
except ValueError:
    print('Inseriu um valor inaceitável')
print(quadrado.area())
print(quadrado)
