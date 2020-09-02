numero = input('Digite um número: ')

unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]

tamanho = len(numero)

resposta= []

try:
    int(numero)
    res = True
except:
    res = False
    print('\nDigite o valor em Int que seja válido!')

if res == True:
    for i in range(0, tamanho):
        for j in range(0, 10):
            if int(numero[i][0]) == j:
                resposta.append(str(unidades[j]))



print("Os números por extenso: ",resposta)

