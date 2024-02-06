import colorama

colorama.init()  # para iniciar

nome_de_usuario = 'Juliana'


def imprimir(texto, nivel='info'):
    if nivel.lower() == 'info':
        print(colorama.Fore.LIGHTMAGENTA_EX + f'Info: ', end='')
        print(colorama.Style.RESET_ALL + texto)
    elif nivel.lower() == 'aviso':
        print(colorama.Fore.YELLOW + f'Aviso: ', end='')
        print(colorama.Style.RESET_ALL + texto)
    elif nivel.lower() == 'erro':
        print(colorama.Fore.RED + f'Erro: ', end='')
        print(colorama.Style.RESET_ALL + texto)
    else:
        print(colorama.Fore.RED + 'Erro interno = nível desconhecido de mensagem' +
              colorama.Style.RESET_ALL)
