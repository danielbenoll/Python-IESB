lista= input("Coloque o Valor da peça 1, a quantidade de peças 1 ... "
                   ", o Valor da peça 2, a quantidade de peças 2, ..."
                   "e o valor do IPI. Tudo separado por espaço: ").split()
if len(lista) == 5:
    try:  #  VERIFICA SE VAL 1 É FLOAT
        float(lista[0])
        res1 = True
    except ValueError:
        print("Dado inválido, insira um valor em FLOAT")
        res1 = False
    try:# VERIFICA SE QDE 1 É INT
        int(lista[1])
        res2 = True
    except ValueError:
        print("Dado inválido, insira um valor em INT")
        res2 = False
    try:# VERIFICA SE VAL 2 É FLOAT
        float(lista[2])
        res3 = True
    except ValueError:
        print("Dado inválido, insira um valor em FLOAT")
        res4 = False
    try:  # VERIFICA SE QDE 2 É INT
        int(lista[3])
        res4 = True
    except ValueError:
        print("Dado inválido, insira um valor numérico")
        res4 = False
    try:  # VERIFICA SE IPI É INT
        int(lista[4])
        res5 = True
    except ValueError:
        print("Dado inválido, insira um valor numérico")
        res5 = False
    if res1 == True and res2 == True and res3 == True and res4 == True and res5 == True:
        Val1 = float(lista[0])
        Qde1 = float(lista[1])
        Val2 = float(lista[2])
        Qde2 = float(lista[3])
        IPI = float(lista[4])
        if Val1 < 0 or Qde1 < 0 or Val2 < 0 or Qde2 < 0 or IPI < 0:
            print("Valor inválido detectado")
        else:
            print('Valor a ser pago: ', (Val1 * Qde1)+(Val2 * Qde2)*(IPI/100 + 1))
else:
    print("Quantidades de dados inválidos!!")