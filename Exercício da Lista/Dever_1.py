A1 = input('Digite a 1º nota do aluno: ')
A2 = input('Digite a 2º nota do aluno: ')
faltas = input('Digite quantas faltas o aluno teve: ')

try:
    float(A1)
    float(A2)
    res1 = True
except:
    res1 = False
    print('\nDigite uma Nota em float que seja válido!')
try:
    float(faltas)
    res2 = True
    faltas = float(faltas)
except:
    res2 = False
    print('\nDigite um valor de Faltas em int que seja válido!')

if res1 == True and res2 == True:
    if faltas >= 0 and faltas <= 90:
        A1 = float(A1)
        A2 = float(A2)
        if A1 >= 0 and A1 <= 10:
            if ((A1 + A2) / 2) >= 9 and ((A1 + A2) / 2) <= 10 and faltas < 22.5:
                print("\nAprovado com SS com nota igual a: ", ((A1 + A2) / 2))
            elif ((A1 + A2) / 2) >= 7 and ((A1 + A2) / 2) <= 8.9 and faltas < 22.5:
                print("\nAprovado com MS com nota igual a: ", ((A1 + A2) / 2))
            elif ((A1 + A2) / 2) >= 5 and ((A1 + A2) / 2) <= 6.9 and faltas < 22.5:
                print("\nAprovado com MM com nota igual a: ", ((A1 + A2) / 2))
            elif ((A1 + A2) / 2) >= 3 and ((A1 + A2) / 2) <= 4.9 and faltas < 22.5:
                print("\nReprovado com MI com nota igual a: ", ((A1 + A2) / 2))
            elif ((A1 + A2) / 2) >= 0.1 and ((A1 + A2) / 2) <= 2.9 and faltas < 22.5:
                print("\nReprovado com II com nota igual a: ", ((A1 + A2) / 2))
            elif ((A1 + A2) / 2) == 0 and faltas < 22.5:
                print("\nReprovado com SR")
            elif float(faltas) >= 22.5:
                print("\nReprovado por número de Faltas igual a: ", faltas)
        else:
            print("\nDados inseridos não válidos, insira os valores da Nota entre 0 a 10")
    else:
        print('\nO número de Faltas deve estar entre 0 e 90')