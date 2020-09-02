"""
###############################

#Questão 1

import pandas as pd
dados ={'matematica': [60, 58, 73, 51, 54, 75, 48, 72, 75, 83, 62, 52], 'musica': [80, 62, 70, 83, 62, 92, 79, 88, 54, 82, 64, 69]}
correlacao = pd.DataFrame(dados,columns=['matematica','musica'])
Matrix = correlacao.corr()
print(Matrix)

print('\nA Correlação de Pearson de "Música" com "Matemática": indica correlação desprezível de 1,16.')


###############################

#Questão 2

# O que se pode dizer com base no valor deste coeficiente de r=0,207 é que indica uma correlação desprezível.
print("O que se pode dizer com base no valor deste coeficiente de r=0,207 é que indica uma correlação desprezível.")


###############################

#Questão 3

import pandas as pd
dados ={'Anos de serviço (x)': [2 ,3, 4, 5, 4, 6, 7, 8, 8, 10], 'Nº de clientes (y)': [48, 50, 56, 52, 43, 60, 62, 58, 64, 72]}
correlacao = pd.DataFrame(dados,columns=['Anos de serviço (x)','Nº de clientes (y)'])
Matrix = correlacao.corr()
print(Matrix)

print('\nA Correlação de "Pearson de Anos de serviço" com "Nº de clientes": indica uma correlação forte de 0,87.')


###############################

#Questão 4

import pandas as pd
dados ={'X': [12,16,18,20,28,30,40,48,50,54], 'Y': [7.2, 7.4, 7, 6.5, 6.6, 6.7, 6, 5.6, 6, 5.5]}
correlacao = pd.DataFrame(dados,columns=['X','Y'])
Matrix = correlacao.corr()
print(Matrix)

print('\nA Correlação de Pearson de "X" com "Y": indica uma correlação muito forte de 0,94.')


###############################

#Questão 5

import statistics
import pandas as pd

x1 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
sx1=0
y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
sy1=0

x2 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
sx2=0
y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
sy2=0

x3 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
sx3=0
y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
sy3=0

x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
sx4=0
y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.5, 5.56, 7.91, 6.89]
sy4=0

for _ in x1:
    sx1 = _ + sx1
sx1 = sx1/ 11

for _ in y1:
    sy1 = _ + sy1

sy1 = sy1 / 11

dados1 ={'X': x1, 'Y': y1}
correlacao1 = pd.DataFrame(dados1,columns=['X','Y'])
Matrix1 = correlacao1.corr()
print(Matrix1)

print("\nA média do Conjunto 1 é de :", round(statistics.mean([sx1, sy1]),2))
print("O desvio padrão do Conjunto 1 é de :", round(float(statistics.stdev([sx1, sy1])),2))
print("O coeficiente da correlação do Conjunto 1 é de : 0,81 e indica uma correlação forte")

for _ in x2:
    sx2 = _ + sx2
sx2 = sx2/ 11

for _ in y2:
    sy2 = _ + sy2

sy2 = sy2 / 11

dados2 ={'X': x2, 'Y': y2}
correlacao2 = pd.DataFrame(dados2,columns=['X','Y'])
Matrix2 = correlacao2.corr()
print(Matrix2)

print("\nA média do Conjunto 2 é de :", round(statistics.mean([sx2, sy2]),2))
print("O desvio padrão do Conjunto 2 é de :", round(float(statistics.stdev([sx2, sy2])),2))
print("O coeficiente da correlação do Conjunto 2 é de : 0,81 e indica uma correlação forte")

for _ in x3:
    sx3 = _ + sx3
sx3 = sx3/ 11

for _ in y3:
    sy3 = _ + sy3

sy3 = sy3 / 11

dados3 ={'X': x3, 'Y': y3}
correlacao3 = pd.DataFrame(dados3,columns=['X','Y'])
Matrix3 = correlacao3.corr()
print(Matrix3)

print("\nA média do Conjunto 3 é de :", round(statistics.mean([sx3, sy3]),2))
print("O desvio padrão do Conjunto 3 é de :", round(float(statistics.stdev([sx3, sy3])),2))
print("O coeficiente da correlação do Conjunto 3 é de : 0,81 e indica uma correlação forte")

for _ in x4:
    sx4 = _ + sx4
sx4 = sx4 / 11
print(sx4)
for _ in y4:
    sy4 = _ + sy4

sy4 = sy4 / 11

dados4 ={'X': x4, 'Y': y4}
correlacao4 = pd.DataFrame(dados4,columns=['X','Y'])
Matrix4 = correlacao4.corr()
print(Matrix4)

print("\nA média do Conjunto 4 é de :", round(statistics.mean([sx4, sy4]), 2))
print("O desvio padrão do Conjunto 4 é de :", round(float(statistics.stdev([sx4, sy4])), 2))
print("O coeficiente da correlação do Conjunto 4 é de : 0,81 e indica uma correlação forte")

"""
###############################

#Questão 6

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

alimentacao = [4, 5, 1, 3, 6, 2]
exercicios = [1, 3, 2, 4, 5, 6]
rodizio = [3, 1, 2, 6, 4, 5]

dados ={'Alimentação': alimentacao, 'Exercícios': exercicios, 'Rodízio': rodizio}
correlacao = pd.DataFrame(dados,columns=['Alimentação','Exercícios', 'Rodízio'])
Matrix = correlacao.corr()
sn.heatmap(Matrix, annot=True)
plt.show()

