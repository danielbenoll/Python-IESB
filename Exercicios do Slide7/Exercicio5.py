valores=input('Insira 3 valores separados por espaço: ').split()
if len(valores) == 3:
    try:
        int(valores[0])
        int(valores[1])
        int(valores[2])
        res = True
    except:
        res = False

    if res == True:
        numeros = [int(valores[0]), int(valores[1]), int(valores[2])]
        numeros.sort()
        print('Os números ordenados são: ', numeros)
    else:
        print('Insira valores inteiros válidos!')
else:
    print('Insira somente 3 valores!')