import random
import math

arquivo = open('valores.txt', 'w')

for i in range(0,100):
    vec = round(random.uniform(0.0, 200.0), 4)
    arquivo.write(str(vec))
    arquivo.write(' ')

arquivo.close()

arquivo = open('valores.txt','r')
for linha in arquivo:
    linha

arquivo.close()

num = linha.split()

media = 0.0
varianca = 0.0
somaVar = 0.0

for i in range(0, 100):
    media = media + float(num[i])

Media = round(media / len(num),4)

for i in range(0, 100):
    varianca = math.pow((float(num[i]) - Media),2)
    #print(varianca)
    somaVar = varianca + somaVar

varMed = round(somaVar / len(num),4)
desvio = round(varMed ** 0.5,4)

print("A média dos 100 números aleatórios é de: ", Media)
print("A variância dos 100 números aleatórios é de: ", varMed)
print("O desvio padrão dos 100 números aleatórios é de: ", desvio)