import sys

while True:

    j1 = 'X'
    j2 = 'O'
    primeiro = 'Jogador 1'
    p1, p2, p3, p4, p5, p6, p7, p8, p9 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    lv = 'livre'
    pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9 = lv, lv, lv, lv, lv, lv, lv, lv, lv
    jogada = 0
    turnos = 0
    vencedor = ''

    tabuleiro_inicial = '''
Bem-vindo ao Jogo da Velha!
O jogador 1 usará o X eo Jogador 2 usará o O
Jogo atual:

     |     |     
  7  |  8  |  9  
_____|_____|_____
     |     |    
  4  |  5  |  6  
_____|_____|_____
     |     |     
  1  |  2  |  3  
     |     |     
    '''

    print(tabuleiro_inicial)


    def atualizar_tabuleiro():
        global p1, p2, p3, p4, p5, p6, p7, p8, p9
        tabuleiro = '''
Jogo atual:
     |     |             |     |   
  7  |  8  |  9       {}  |  {}  |  {}
_____|_____|_____   _____|_____|_____
     |     |             |     |
  4  |  5  |  6       {}  |  {}  |  {}
_____|_____|_____   _____|_____|_____
     |     |             |     |
  1  |  2  |  3       {}  |  {}  |  {}
     |     |             |     |

        '''.format(p7, p8, p9, p4, p5, p6, p1, p2, p3, )
        print(tabuleiro)

    def jogada_j1():
        global jogada

        while True:
            try:
                jogada = int(input('Jogador 1, insira a posição a preencher (1 até 9): '))
                break
            except ValueError:
                print('\nValor Inválido, tente novamente!\n')



    def rotina_j1():
        global jogada
        global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

        msg_ocupado = '\nEste espaço já está ocupado!\n'

        while jogada not in range(1, (9 + 1)):
            jogada_j1()

            if jogada not in range(1, (9 + 1)):
                print('\nValor Inválido, tente novamente!\n')

        while jogada == 1 and pos1 == 'ocupada' or \
            jogada == 2 and pos2 == 'ocupada' or \
            jogada == 3 and pos3 == 'ocupada' or \
            jogada == 4 and pos4 == 'ocupada' or \
            jogada == 5 and pos5 == 'ocupada' or \
            jogada == 6 and pos6 == 'ocupada' or \
            jogada == 7 and pos7 == 'ocupada' or \
            jogada == 8 and pos8 == 'ocupada' or \
                jogada == 9 and pos9 == 'ocupada':
            print(msg_ocupado)
            rotina_j1()

    def atualizar_jogadas_j1():
        global jogada
        global p1, p2, p3, p4, p5, p6, p7, p8, p9
        global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

        if jogada == 1:
            p1 = j1
            pos1 = 'ocupada'
        elif jogada == 2:
            p2 = j1
            pos2 = 'ocupada'
        elif jogada == 3:
            p3 = j1
            pos3 = 'ocupada'
        elif jogada == 4:
            p4 = j1
            pos4 = 'ocupada'
        elif jogada == 5:
            p5 = j1
            pos5 = 'ocupada'
        elif jogada == 6:
            p6 = j1
            pos6 = 'ocupada'
        elif jogada == 7:
            p7 = j1
            pos7 = 'ocupada'
        elif jogada == 8:
            p8 = j1
            pos8 = 'ocupada'
        elif jogada == 9:
            p9 = j1
            pos9 = 'ocupada'



    def jogada_j2():
        global jogada

        while True:
            try:
                jogada = int(input('Jogador 2, insira a posição a preencher (1 até 9): '))
                break
            except ValueError:
                print('\nValor Inválido, tente novamente!\n')


    def rotina_j2():
        global jogada
        global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

        msg_ocupado = '\nEste espaço já está ocupado!\n'

        jogada_j2()

        while jogada not in range(1, (9 + 1)):
            jogada_j2()

            if jogada not in range(1, (9 + 1)):
                print('\nValor Inválido, tente novamente!\n')

        while jogada == 1 and pos1 == 'ocupada' or \
                jogada == 2 and pos2 == 'ocupada' or \
                jogada == 3 and pos3 == 'ocupada' or \
                jogada == 4 and pos4 == 'ocupada' or \
                jogada == 5 and pos5 == 'ocupada' or \
                jogada == 6 and pos6 == 'ocupada' or \
                jogada == 7 and pos7 == 'ocupada' or \
                jogada == 8 and pos8 == 'ocupada' or \
                jogada == 9 and pos9 == 'ocupada':
            print(msg_ocupado)
            rotina_j2()


    def atualizar_jogadas_j2():
        global jogada
        global p1, p2, p3, p4, p5, p6, p7, p8, p9
        global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

        if jogada == 1:
            p1 = j2
            pos1 = 'ocupada'
        elif jogada == 2:
            p2 = j2
            pos2 = 'ocupada'
        elif jogada == 3:
            p3 = j2
            pos3 = 'ocupada'
        elif jogada == 4:
            p4 = j2
            pos4 = 'ocupada'
        elif jogada == 5:
            p5 = j2
            pos5 = 'ocupada'
        elif jogada == 6:
            p6 = j2
            pos6 = 'ocupada'
        elif jogada == 7:
            p7 = j2
            pos7 = 'ocupada'
        elif jogada == 8:
            p8 = j2
            pos8 = 'ocupada'
        elif jogada == 9:
            p9 = j2
            pos9 = 'ocupada'

    def checar_vencedor():
        global j1, j2, turnos, vencedor, pts_jogador, pts_pc
        global p1, p2, p3, p4, p5, p6, p7, p8, p9

        if p1 == j1 and p2 == j1 and p3 == j1 or \
           p1 == j1 and p4 == j1 and p7 == j1 or \
           p1 == j1 and p5 == j1 and p9 == j1 or \
           p2 == j1 and p5 == j1 and p8 == j1 or \
           p3 == j1 and p5 == j1 and p7 == j1 or \
           p3 == j1 and p6 == j1 and p9 == j1 or \
           p4 == j1 and p5 == j1 and p6 == j1 or \
           p7 == j1 and p8 == j1 and p9 == j1:
            print('Jogador 1 Ganhou!\n')
            pts_jogador += 1
            vencedor = 'Jogador 1'
            sys.exit(0)

        if p1 == j2 and p2 == j2 and p3 == j2 or \
           p1 == j2 and p4 == j2 and p7 == j2 or \
           p1 == j2 and p5 == j2 and p9 == j2 or \
           p2 == j2 and p5 == j2 and p8 == j2 or \
           p3 == j2 and p5 == j2 and p7 == j2 or \
           p3 == j2 and p6 == j2 and p9 == j2 or \
           p4 == j2 and p5 == j2 and p6 == j2 or \
           p7 == j2 and p8 == j2 and p9 == j2:
            print('Jogador 2 Ganhou!\n')
            pts_pc += 1
            vencedor = 'Jogador 2'
            sys.exit(0)

    def atualizar_tudo():
        global jogada
        global turnos
        global vencedor

        if primeiro == 'Jogador 1':
            rotina_j1()
            atualizar_jogadas_j1()
            atualizar_tabuleiro()
            checar_vencedor()

            turnos += 1

            if turnos == 9:
                print('NÓS EMPATAMOS!\n')
                turnos = 9
                vencedor = 'EMPATE'
                sys.exit(0)

            rotina_j2()
            atualizar_jogadas_j2()
            atualizar_tabuleiro()
            checar_vencedor()

            turnos += 1

            if turnos == 9:
                print('NÓS EMPATAMOS!\n')
                turnos = 9
                vencedor = 'EMPATE'
                sys.exit(0)


        jogada = 0
    while turnos < 9:
        atualizar_tudo()