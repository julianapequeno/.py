def maior_ponto_da_figura(listaPontosFigura):
    maior = int(0)
    for i in listaPontosFigura:
        if(int(i[0]) > int(maior)):
            maior = i[0]
    return maior
def dentro_da_figura():
    #para verificar se os dois pontos estão em lados opostos um deve estar POSITIVO e outro NEGATIVO
    pass
def rodar():
    N,M = input().split(" ")
    N = int(N) #pontos
    M = int(M) #cliques

    dic = {}
    flag = 0
    listaPontosFigura = []
    for i in range(0,N):
        x,y = input().split(" ")
        par = [x,y]
        listaPontosFigura.append(par)
    for i in range(0,M):
        A,x,y = input().split(" ")
        dic[A] = [x,y]

    xMax = 0
    xMax = maior_ponto_da_figura(listaPontosFigura)

    quant_lados = len(listaPontosFigura) #1-2 | 2-3 | 3-4 | 4-5 | 5-1
    retorno = 0
    for ii in dic:
        clique = dic.get(ii)
        pontoC = [xMax, clique[1]] #[xMax,y_do_clique]
        for i in listaPontosFigura:
            #print(i)
            index  = listaPontosFigura.index(i)+1
            if(listaPontosFigura.index(i)+1 == len(listaPontosFigura)):
                index = 0
                continue
            pontos = [i,listaPontosFigura[index]]
            retorno = testa_linha_com_reta(pontos, pontoC, clique)
        if (retorno==True):
            print(ii)
def testa_linha_com_reta(pontos, pontoC,clique):
    #4pontos -> pontos[] são os dois pontos da reta, clique é o clique do mouse e pontoC é o verificador com o maior X para ver se clicou dentro
    z = (int(pontos[1][0])-int(pontos[0][0]))*(int(clique[1])-int(pontos[0][1])) - (int(pontos[1][1])-int(pontos[0][1]))*(int(clique[0])-int(pontos[0][0]))
    z2 = (int(pontos[1][0])-int(pontos[0][0]))*(int(pontoC[1])-int(pontos[0][1])) - (int(pontos[1][1])-int(pontos[0][1]))*(int(pontoC[0])-int(pontos[0][0]))

    if(z <= 0):
        c = 'D'
    else:
        c = 'E'

    if(z2 <= 0):
        c2 = 'D'
    else:
        c2 = 'E'
#    print(c,c2)
    if(c != c2):
        return True
if(__name__ == '__main__'):
    rodar()