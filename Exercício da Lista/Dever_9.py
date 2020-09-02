import string

arquivo = open('bible.txt','r')

for listas in arquivo:
    listas = arquivo.readlines()

arquivo.close()

texto = string.capwords(str(listas))
texto.upper()

arquivo = open('auth.log.4','w')
    a
