val1=input('Insira o 1º valor do triangulo: ')
val2=input('Insira o 2º valor do triangulo: ')
val3=input('Insira o 3º valor do triangulo: ')

try:
    float(val1)
    float(val2)
    float(val3)
    res = True
except:
    res = False
if res==True:
    val1= float(val1)
    val2 = float(val2)
    val3 = float(val3)
    if val1 == val2 and val1==val3:
        print('Triangulo Equilátero!')
    elif (val1 == val2) or (val2==val3) or (val3 == val2):
        print('Triangulo Isósceles!')
    else:
        print('Triângulo Escaleno!')
else:
    print('Insira valores numéricos!')
