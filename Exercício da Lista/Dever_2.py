segundos = input('Digite a quantidade Segundos para obter horas, minutos e segundo: ')

try:
    int(segundos)
    res = True
    segundos = int(segundos)
except:
    res = False
    print('\nDigite o valor dos Segundos em int que seja válido!')

if res == True and segundos > 0:
    horas = segundos // 3600
    minutos = segundos % 3600 // 60
    Segundos = (segundos % 3600) - 60 * minutos
    print('São: ')
    if horas > 1:
        print(horas,'horas ')
    elif horas == 1:
        print(horas, 'hora ')
    if minutos > 0:
        print(minutos, 'minutos ')
    elif minutos == 1:
        print(minutos, 'minuto ')
    if Segundos > 0:
        print(Segundos, 'segundos ')
    elif Segundos == 1:
        print(Segundos, 'segundo ')
else:
    print('Valor incorreto! Insira um valor dos Segundos maior que zero')