class ingresso:
    def __init__(self):
        self.dia = int(input("1 = domingo\n2 = segunda\n3 = terça\n4 = quarta\n5 = quinta\n6 = sexta\n7 = sábado\n"))
        self.hora = int(input("Horário: "))
        self.meia = int(input("0 = inteira\n1 = meia\n"))
        self.valor = 0

    def calc(self):
        # Definir valor base
        if self.dia == 4:
            self.valor = 8
        elif self.dia in [2, 3, 5]:
            self.valor = 16
        elif self.dia in [1, 6, 7]:
            self.valor = 20

        # Aumento após 17h
        if self.hora >= 17:
            self.valor *= 1.5

        # Meia entrada
        if self.meia == 1:
            self.valor /= 2

        return self.valor


x = ingresso()
v = x.calc()
print(f"O valor do ingresso é R${v:.2f}")
