altura=input('Insira sua altura em metros: ')
sexo=input('Insira seu sexo, M pra masculinho, e F pra feminino: ')

try:
    float(altura)
    res = True
except:
    res = False

if res == True and len(sexo) == 1:
    if float(altura)>.25 and float(altura)<2.71:
        if sexo.lower()=='m':
            print('Peso ideal: ', round(72.7*float(altura)-58,2), 'Kg')
        elif sexo.lower()=='f':
            print('Peso ideal: ', round(62.1*float(altura)-44.7,2), 'Kg')
        else:
            print('Insira o sexo correto!!')
    else:
        print('Insira uma altura válida entre 0.25 e 2.71')
else:
    print('Dados inválidos!')