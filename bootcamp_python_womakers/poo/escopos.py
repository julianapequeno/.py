bebida = 'refrigerante'


def cardapio():
    comida = 'hamburguer'
    bebida = 'suco'  # tá criando uma nova ao inves de alter
    # alterar a variável global
    print('comida: ', comida)
    print('bebida: ', bebida)  # print a nova


def cardapio_global():
    global bebida  # indica que nesta funcao quando essa variável for
    # chamada, é para referenciar a variável global
    comida = 'hamburguer'
    bebida = 'suco'
    print('comida: ', comida)
    print('bebida: ', bebida)  # print a nova


print('TESTE SEM o global')
cardapio()
print('bebida fora: ', bebida)

print('TESTE COM o global:')
cardapio_global()
print('bebida fora: ', bebida)
