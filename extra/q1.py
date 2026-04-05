class Energia:
    def __init__(self, mes, ano, consumo):
        self.mes = mes
        self.ano = ano
        self.consumo = consumo

    def calc(self):
        if self.consumo <= 50:
            conta = 30
        elif self.consumo <= 100:
            conta = 30 + (self.consumo - 50) * 0.8
        else:
            conta = 30 + 50 * 0.8 + (self.consumo - 100) * 1.2
        
        return conta

mes = input("Digite o mês: ")
ano = input("Digite o ano: ")
consumo = int(input("Digite o consumo em kWh: "))

c = Energia(mes, ano, consumo)
valor = c.calc()

print(f"O valor da conta de energia foi de R${valor}")
