qde=input('Insira a quantidade de maçãs: ')

try:
    int(qde)
    res = True
except:
    res = False
if res == True and int(qde)>0:
    if int(qde) > 11:
        print('A conta deu:', int(qde)*.25)
    else:
        print('A conta deu:', int(qde) * .3)
else:
    print('Insira uma quantidade de maçãs válida!')