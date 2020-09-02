val1=input('Insira o 1º angulo do triangulo: ')
val2=input('Insira o 2º angulo do triangulo: ')
val3=input('Insira o 3º angulo do triangulo: ')

try:
    float(val1)
    float(val2)
    float(val3)
    res = True
except:
    res = False
if res == True:
    val1 = float(val1)
    val2 = float(val2)
    val3 = float(val3)
    if val1 <=0 or val1>=180 or val2 <=0 or val2>=180 or val3 <=0 or val3>=180:
        print('Insira angulos maiores que 0 e menores que 180 graus')
    elif (val1+val2+val3)!= 180:
        print('Não é um triângulo!')
    else:
        if val1==90 or val2==90 or val3==90:
            print('Triangulo retângulo!')
        elif val1>90 or val2>90 or val3>90:
            print('Triangulo obtusângulo!')
        else:
            print('Triangulo acutângulo!')
else:
    print('Insira valores numéricos!')