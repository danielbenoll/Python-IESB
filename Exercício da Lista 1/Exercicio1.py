#anos=input('Digite quantos anos você tem: ')
#meses=input('Digite quantos após o seu aniversário, você tem: ')
#anos=input('Digite quantos anos você tem')
#print(anos)

lista_dados= input("coloque quantos anos, meses, dias voce tem, separado por espaço: ").split()

if (lista_dados[0].isnumeric() and lista_dados[1].isnumeric() and lista_dados[2].isnumeric()) == False:
    print("Dados invalidos!")
else:
    ano=int(lista_dados[0])
    mes = int(lista_dados[1])
    dia = int(lista_dados[2])
    if(ano<0 or ano>110 or mes<0 or mes>11 or dia >30):
        print("Dados invalidos!")
    else:
        print("Quantidade de dias: " + str(ano*365+mes*30+dia))

#print(lista_dados[0].isnumeric())

