def soma(NUM1, NUM2):
    so = NUM1+NUM2

    file = "arquivo.txt"
    # open

    # open para escrita

    arquivo_escrita = open(file, 'w')
    arquivo_escrita.write(f'A soma resultou: {so}')
    arquivo_escrita.close()

    # open para leitura
    arquivo_leitura = open(file, 'r')
    leitura = arquivo_leitura.read()
    print(leitura)
    arquivo_leitura.close()

    # open para arquivo binário
    arquivo_binario = open(file, 'wb')
    arquivo_binario.write('01101110111100101010')
    arquivo_binario.close()


soma(5, 9)
