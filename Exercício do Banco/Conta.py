class Conta():
    def __init__(self, dono, saldo = 0):
        self.dono = dono
        self.saldo = saldo

    def __str__(self):
        return f'\nBem-vindo(a) {self.dono}! Seu saldo atual é R$0.0'

    def deposito (self, qde_dep):

        self.saldo += int(qde_dep)

        print('Depósito de R$'+qde_dep+'.0 com sucesso!')
        print('Saldo atual de R$', float(self.saldo))

    def saque(self, qde_saque):

        if int(qde_saque) > self.saldo:
            print('Saldo insuficiente! Saldo atual de R$', float(self.saldo))
        else:
            self.saldo -= int(qde_saque)

            print('Saque de R$' + qde_saque + '.0 com sucesso!')
            print('Saldo atual de R$', float(self.saldo))

dono = input('Digite o seu nome: ')
operacao = 0

conta = Conta(dono)
print(conta)

while operacao != 3:
    operacao = input('\nSelecione a sua operação:\n'
                     '(1) Depósito ou (2) Saque ou (3) Sair ')
    try:
        int(operacao)
        res = True
    except:
        res = False
        print('Operação inválida!')

    if res == True:
        if int(operacao) == 1:
            qde_dep = input('Insira o valor do depósito: ')

            try:
                int(qde_dep)
                dep = True
            except:
                dep = False
                print('Valor inválido!')

            if dep == True:
                conta.deposito(qde_dep)

        elif int(operacao) == 2:
            qde_saque = input('Insira o valor do saque: ')

            try:
                int(qde_saque)
                saque = True
            except:
                saque = False
                print('Valor inválido!')

            if saque == True:
                conta.saque(qde_saque)

        elif int(operacao) == 3:
            print('Até mais!')
            break
        else:
            print('Operação inválida!')