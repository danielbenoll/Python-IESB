valor_str= input("Insira seu salário: ")

try:  # VERIFICA SE valor_str 1 É FLOAT
    float(valor_str)
    res1 = True
except ValueError:
    print("Dado inválido, insira um valor em FLOAT")
    res1 = False

if res1 == True :
    if float(valor_str)>=0:
        print("Ganha: ", round(float(valor_str)/788,2), "salários minímos")
    else:
        print("Insira um salário positivo!")
else:
    print("Dado inválido, insira um valor numérico!")