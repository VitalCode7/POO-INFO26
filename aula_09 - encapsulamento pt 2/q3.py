class conta_banc:
    def __init__(self, nome, numero, saldo):
        self.__nome = nome
        self.__numero = numero
        self.__saldo = saldo
    
    def set_nome(self, n):
        self.__nome = n
    
    def set_numero(self, num):
        self.__numero = num
    
    def set_saldo(self, s):
        self.__saldo = s
    
    def get_nome(self):
        return self.__nome
    
    def get_numero(self):
        return self.__numero
    
    def get_saldo(self):
        return self.__saldo
    
    def sacar(self):
        saque = float(input("Quanto você deseja sacar? "))
        self.__saldo -= saque
        return self.__saldo

    def depositar(self):
        deposito = float(input("Quanto você deseja depositar? "))
        self.__saldo += deposito
        return self.__saldo

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
print(f"Saldo final: {x.__saldo}")
