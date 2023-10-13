numero = int(input("Digite um número: "))
N = 100
multiplo = 1

listDivisiveis = []

for i in range(0,N):
    if(i==0):
        continue
    elif(numero%i==0 ):
        listDivisiveis.append(i)

print("São exatamente {} números que dividem o {}!".format(len(listDivisiveis), numero))
if(len(listDivisiveis)==2):
    if(listDivisiveis[0] == 1 and listDivisiveis[1] == numero):
        print("O número {} também é um número primo!".format(numero))
print("Aqui estão eles: {}".format(listDivisiveis))

