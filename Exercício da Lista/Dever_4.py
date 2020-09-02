num = input('Digite um número entre 0 a 999: ')

romanos = ['CM', 'DCCC', 'DCC', 'DC', 'D', 'CD', 'CCC', 'CC', 'C', 'XC', 'LXXX', 'LXX', 'LX', 'L', 'XL', 'XXX', 'XX', 'X', 'IX', 'VIII', 'VII', 'VI', 'V', 'IV', 'III', 'II', 'I']

resultado= []

numBase = num

try:
    int(num)
    res = True
    num = int(num)
except:
    res = False
    print('\nDigite o valor em Int que seja válido!')

if res == True and num >= 0 and num < 1000:
    # print(num)
    if num >= 900:
        resultado.append(str(romanos[0]))
        num = num - 900
    if num >= 800:
        resultado.append(str(romanos[1]))
        num = num - 800
    if num >= 700:
        resultado.append(str(romanos[2]))
        num = num - 700
    if num >= 600:
        resultado.append(str(romanos[3]))
        num = num - 600
    if num >= 500:
        resultado.append(str(romanos[4]))
        num = num - 500
    if num >= 400:
        resultado.append(str(romanos[5]))
        num = num - 400
    if num >= 300:
        resultado.append(str(romanos[6]))
        num = num - 300
    if num >= 200:
        resultado.append(str(romanos[7]))
        num = num - 200
    if num >= 100:
        resultado.append(str(romanos[8]))
        num = num - 100
    if num >= 90:
        resultado.append(str(romanos[9]))
        num = num - 90
    if num >= 80:
        resultado.append(str(romanos[10]))
        num = num - 80
    if num >= 70:
        resultado.append(str(romanos[11]))
        num = num - 70
    if num >= 60:
        resultado.append(str(romanos[12]))
        num = num - 60
    if num >= 50:
        resultado.append(str(romanos[13]))
        num = num - 50
    if num >= 40:
        resultado.append(str(romanos[14]))
        num = num - 40
    if num >= 30:
        resultado.append(str(romanos[15]))
        num = num - 30
    if num >= 20:
        resultado.append(str(romanos[16]))
        num = num - 20
    if num >= 10:
        resultado.append(str(romanos[17]))
        num = num - 10
    if num >= 9:
        resultado.append(str(romanos[18]))
        num = num - 9
    if num >= 8:
        resultado.append(str(romanos[19]))
        num = num - 8
    if num >= 7:
        resultado.append(str(romanos[20]))
        num = num - 7
    if num >= 6:
        resultado.append(str(romanos[21]))
        num = num - 6
    if num >= 5:
        resultado.append(str(romanos[22]))
        num = num - 5
    if num >= 4:
        resultado.append(str(romanos[23]))
        num = num - 4
    if num >= 3:
        resultado.append(str(romanos[24]))
        num = num - 3
    if num >= 2:
        resultado.append(str(romanos[25]))
        num = num - 2
    if num >= 1:
        resultado.append(str(romanos[26]))
        num = num - 1
    print("\nO número: ", numBase ,", em números romanos é igual:", resultado)
else:
    print('\nO número deve estar entre 0 e 90')