val1=input('Insira o 1º valor numerico: ')
val2=input('Insira o 2º valor numerico: ')
val3=input('Insira o 3º valor numerico: ')

try:
    float(val1)
    float(val2)
    float(val3)
    res = True
except:
    res = False
if res==True:
    print('Maior numero: ', max(float(val1),float(val2),float(val3)))