class conta_banc:
    def __init__(self):
        self.nome = input("Digite seu nome: ")
        self.num = input("Digite o número da sua conta: ")
        self.saldo = float(input("Digite seu saldo: "))

    def sacar(self):
        saque = float(input("Quanto você deseja sacar? "))
        self.saldo -= saque
        return self.saldo

    def depositar(self):
        deposito = float(input("Quanto você deseja depositar? "))
        self.saldo += deposito
        return self.saldo

    def menu(self):
        i = 1
        while i != 0:
            i = int(input("0 = sair\n1 = Saque\n2 = Depósito\n"))
            if i == 1:
                self.sacar()
            elif i == 2:
                self.depositar()

x = conta_banc()
x.menu()
print(f"Saldo final: {x.saldo}")
