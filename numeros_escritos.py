def bancodedados():
    dicionario = {"zero":0,"um": 1, "dois": 2, "tres": 3, "quatro": 4, "cinco": 5, "seis": 6, "sete": 7, "oito": 8, "nove": 9}
    dicionario2 = {"dez": 10, "vinte": 20, "trinta": 30, "quarenta": 40, "cinquenta": 50, "sessenta": 60, "setenta": 70,
                   "oitenta": 80, "noventa": 90}
    dicionario3 = {"cem": 100, "duzentos": 200, "trezentos": 300, "quatrocentos": 400, "quinhentos": 500,
                   "seiscentos": 600, "setecentos": 700, "oitocentos": 800, "novecentos": 900}
    dicionarios = [dicionario3, dicionario2, dicionario]
    return dicionarios

def rodar():
    numero = int(input("Digite um número entre 0 e 999: "))
    string = str(numero)
    tam_string = len(string)
    numDic = int(string[0])

    dicionarios = []
    dicionarios = bancodedados()
    imprime_numero(dicionarios,tam_string,string,numero,numDic)

def imprime_numero(dicionarios,tam_string, string, numero, numDic):
    flag = False
    indices = False
    for dicionario in dicionarios:
        if (tam_string == 3):
            # centena + dezena + unidade
            for i in dicionario:
                if (numDic * 100 == dicionario[i]):
                    print(i, end=" ")
            tam_string -= 1
            numDic = int(string[1])
            indices = True
            if (numDic * 100 != 0):
                print("e", end=" ")
            continue
        if (tam_string == 2):
            if(not indices and not flag):
                flag = True
                continue
            for i in dicionario:
                if (numDic * 10 == dicionario[i]):
                    print(i, end=" ")
            tam_string -= 1
            if(int(string[len(string) - 1])*10 != 0):
                print("e", end=" ")
            continue
        if (tam_string == 1):  # unidade apenas
            for i in dicionario:
                if (int(string[len(string) - 1]) == dicionario[i]):
                    if(int(string[len(string) - 1])==0 and indices):
                        continue
                    else:
                        print(i, end=" ")
            continue

if(__name__ == '__main__'):
    rodar()