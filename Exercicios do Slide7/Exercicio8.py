import math

qde_lado=input('Insira o lado em cm: ')
med_lado=input('Insira o lado em cm: ')

try:
    int(qde_lado)
    int(med_lado)
    res = True
except:
    res = False
if res == True:
    qde_lado = int(qde_lado)
    med_lado = int(med_lado)
    if qde_lado == 3:
        print('Área de um triângulo regular: ', round( (med_lado*math.sqrt(3))/4,2), 'cm2')
    elif qde_lado == 4:
        print('Área de um quadrado: ', round(med_lado * med_lado,2), 'cm2')
    elif qde_lado <= 5:
        print('Área do pentagono regular: ',  round(((med_lado * med_lado*math.sqrt(3))/4)*5,2), 'cm2')
    elif qde_lado<3:
        print('Não é um poligono')
    else:
        print('Poligono não identificado!')
else:
    print('Insira dados inteiros válidos!')