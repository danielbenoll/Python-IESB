valor1=input('Insira o 1º valor numérico: ')
valor2=input('Insira o 2º valor numérico: ')

try:
    int(valor1)
    res_int = True
except:
    res_int = False
if res_int == False:
    try:
        float(valor1)
        res_float = True
    except:
        res_float = False
        print('\nInsira um valor numérico!')
if float(valor1) == float(valor2):
    print('Insira valores diferentes!!')
else:
    print('O maior número é: ', max(float(valor1), float(valor2)))
