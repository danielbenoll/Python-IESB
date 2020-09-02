saldo = input("Insira um saldo: ")

try:
    float(saldo)
    print("Dado válido")
    res=True
except ValueError:
    print("Dado inválido, insira um valor numérico")
    res = False

print("O seu saldo é igual a: ", float(saldo) * 1.01)