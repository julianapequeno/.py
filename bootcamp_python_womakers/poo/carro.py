# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

class carro:
    def __init__(self):
        self.ligado = False
        self.cor = 'Pink'
        self.modelo = 'HB20'
        self.velocidade = 0

    def liga(self):
        self.ligado = True
        print('Carro ligado')

    def desliga(self):
        self.ligado = False
        print('Carro desligado')

    def acelera(self):
        self.velocidade += 5

    def desacelera(self):
        self.velocidade -= 5


# Crie uma instância da classe carro.

carro = carro()

# Faça o carro "andar" utilizando os métodos da sua classe.
carro.liga()

for _ in range(10):
    carro.acelera()
print(f'Velocidade: {carro.velocidade}')

# Faça o carro "parar" utilizando os métodos da sua classe.
while (carro.velocidade > 0):
    carro.desacelera()
print(f'Velocidade: {carro.velocidade}')

carro.desliga()
