class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def transferir(self, destino, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            destino.saldo += valor
        else:
            print("Saldo insuficiente para transferência")


# criação das contas
contas = []

for i in range(2):
    titular = input("Digite o nome do titular da conta: ")
    saldo = float(input("Digite o saldo da conta: "))
    
    conta = Conta(titular, saldo)
    contas.append(conta)


# exemplo de uso
c1 = contas[0]
c2 = contas[1]

c1.depositar(100)
c1.transferir(c2, 50)

print(f"{c1.titular}: R${c1.saldo}")
print(f"{c2.titular}: R${c2.saldo}")
