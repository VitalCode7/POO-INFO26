class Triangulo:
    def __init__(self):
        self.__b = 0.0
        self.__h = 0.0

    def set_base(self, v):
        if v >= 0:
            self.__b = v
        else:
            raise ValueError()

    def set_altura(self, v):
        if v >= 0:
            self.__h = v
        else:
            raise ValueError()

    def get_base(self):
        return self.__b
    
    def get_altura(self):
        return self.__h
    
    def calc_area(self):
        return self.__b * self.__h / 2


class Circulo:
    def __init__(self):
        self.__raio = 0

    def set_raio(self, v):
        if v < 0:
            raise ValueError("Valor inválido")
        self.__raio = v

    def get_raio(self):
        return self.__raio

    def calc_area(self):
        return 3.14 * self.__raio ** 2

    def calc_circunferencia(self):
        return 2 * 3.14 * self.__raio


class Viagem:
    def __init__(self):
        self.__distancia = 0
        self.__tempo = 0

    def set_distancia(self, d):
        if d <= 0:
            raise ValueError("Valor inválido")
        self.__distancia = d

    def set_tempo(self, t):
        if t <= 0:
            raise ValueError("Valor inválido")
        self.__tempo = t

    def get_distancia(self):
        return self.__distancia

    def get_tempo(self):
        return self.__tempo

    def velocidade_media(self):
        return self.__distancia / self.__tempo


class conta_banc:
    def __init__(self):
        self.__nome = ""
        self.__numero = 0
        self.__saldo = 0.0

    def set_nome(self, n):
        self.__nome = n

    def set_num(self, num):
        self.__numero = num

    def set_saldo(self, s):
        self.__saldo = s

    def get_nome(self):
        return self.__nome

    def get_numero(self):
        return self.__numero

    def get_saldo(self):
        return self.__saldo

    def sacar(self, valor):
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente")
        self.__saldo -= valor
        return self.__saldo

    def depositar(self, valor):
        self.__saldo += valor
        return self.__saldo


class Ingresso:
    def __init__(self, dia, hora, meia):
        self.__dia = dia
        self.__hora = hora
        self.__meia = meia
        self.__valor = 0

    def get_dia(self):
        return self.__dia

    def get_hora(self):
        return self.__hora

    def get_meia(self):
        return self.__meia

    def get_valor(self):
        return self.__valor

    def calc(self):
        if self.__dia == 4:
            self.__valor = 8
        elif self.__dia in [2, 3]:
            self.__valor = 16
        else:
            self.__valor = 20

        if self.__hora >= 17:
            self.__valor *= 1.5

        if self.__meia == 's':
            self.__valor /= 2

        return self.__valor


class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1:
                UI.triangulo()
            elif op == 2:
                UI.circulo()
            elif op == 3:
                UI.viagem()
            elif op == 4:
                UI.conta_bancaria()
            elif op == 5:
                UI.ingresso()

    @staticmethod
    def menu():
        print("1-Triângulo, 2-Círculo, 3-Viagem, 4-Conta Bancária, 5-Ingresso, 9-Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def triangulo():
        x = Triangulo()
        x.set_base(float(input("Base: ")))
        x.set_altura(float(input("Altura: ")))
        print(f"Área = {x.calc_area()}")
        print("="*40)

    @staticmethod
    def circulo():
        x = Circulo()
        x.set_raio(float(input("Raio: ")))
        print(f"Área = {x.calc_area()}")
        print(f"Circunferência = {x.calc_circunferencia()}")
        print("="*40)

    @staticmethod
    def viagem():
        x = Viagem()
        x.set_distancia(float(input("Distância: ")))
        x.set_tempo(float(input("Tempo: ")))
        print(f"Velocidade média = {x.velocidade_media()} km/h")
        print("="*40)

    @staticmethod
    def conta_bancaria():
        x = conta_banc()
        x.set_nome(input("Nome: "))
        x.set_num(int(input("Número da conta: ")))
        x.set_saldo(float(input("Saldo inicial: ")))

        operacao = input('Digite "d" (depósito) ou "s" (saque): ').lower()
        valor = float(input("Valor: "))

        if operacao == "d":
            novo = x.depositar(valor)
        elif operacao == "s":
            novo = x.sacar(valor)
        else:
            print("Operação inválida")
            return

        print(f"Conta: {x.get_nome()} | Nº {x.get_numero()} | Saldo: {novo:.2f}")
        print("="*40)

    @staticmethod
    def ingresso():
        dia = int(input("Dia (1-7): "))
        hora = int(input("Hora: "))
        meia = input("Meia? (s/n): ").lower()

        x = Ingresso(dia, hora, meia)
        valor = x.calc()

        print(f"Ingresso: R$ {valor:.2f}")
        print("="*40)

UI.main()