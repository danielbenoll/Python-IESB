import random

vetor= []

for i in range(0,100):
    vetor.append(round(random.uniform(0.0, 200.0), 3))

resultado1 = sorted(vetor, key=float)
resultado2 = list(reversed(resultado1))

print("Números ordenados de forma incremental: \n", resultado1)
print("Números ordenados de forma descremental:: \n",resultado2)