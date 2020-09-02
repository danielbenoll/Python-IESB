import datetime
now= datetime.datetime.now()
ano_atual=now.year

ano_informado=input('Insira um ano de nascimento: ')

try:
    int(ano_informado)
    res_int = True
except:
    res_int = False
if res_int==True and (ano_atual-int(ano_informado)<=110) and (int(ano_informado)< ano_atual):
    if ano_atual - int(ano_informado)>=18:
        print("Pode Votar!")
    else:
        print('Não pode votar!')
else:
    print('Insira um número de ano válido!')