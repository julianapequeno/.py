def divisao(a, b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError:
        print('Opa! Erro! Ocorreu uma divisão por zero!')
    except TypeError as e:
        print(f'Erro: O tipo do dado informado está incorreto. Detalhes:  {e}')
    except (ValueError, TypeError):
        print('Both')
    else:
        print('Sem exceções')


divisao(0, 'juliana')
