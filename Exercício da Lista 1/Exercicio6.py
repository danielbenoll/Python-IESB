valor_str= input("Insira um numero inteiro: ")

try:  # VERIFICA SE QDE 1 É INT
    int(valor_str)
    res = True
except ValueError:
    #print("Dado inválido, insira um valor em INT")
    res = False
if res == True:
    print("Numero antecessor: ", int(valor_str) - 1)
    print("Numero sucessor: ", int(valor_str) + 1)
else:
    print("Erro: Insira um número inteiro!")