arquivo = open('0304.txt')

contador = 0

for linha in arquivo:
    correto = linha.replace("\n", "")
    correto = correto.lower()
    reverso = correto[::-1]

    if len(correto) == 1:
        continue
    elif correto == reverso:
        contador = contador + 1

print(contador)