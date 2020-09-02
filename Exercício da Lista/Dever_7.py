import math
import decimal

numero = input('Digite um número: ')
erro = input('O tamanho do erro (máximo ate 4): ')

try:
    int(numero)
    numero = int(numero)
    res1 = True
except:
    res1 = False
    print('\nDigite um valor em Int válido!')
try:
    int(erro)
    erro = int(erro)
    res2 = True
except:
    res2 = False
    print('\nDigite um valor em Int válido!')


if res1 == True and res2 == True:
    if erro>=0 and erro <=4:
        resultado = math.sqrt(numero)
        print(round(resultado, erro))
    else:
        print('O valor do erro tem que estar entre 0 e 4')
else:
    print('Valor inserido está incorreto!')