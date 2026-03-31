class agua:
    def __init__(self, mes, ano, consumo):
        self.mes = mes
        self.ano = ano
        self.consumo = consumo
        self.conta = 0
    def calc_agua(self):
        if self.consumo <= 10:
            self.conta = 38
        if 10 < self.consumo <= 20:
            self.conta = 38 + (self.consumo - 10) * 5
        if self.consumo > 20:
            self.conta = 38 + (10 * 5) + ((self.consumo - 20) * 6)
        return self.conta
    
mes = input("Digite o mês: ")
ano = input("Digite o ano: ")
consumo =int(input("Digite o consumo de água em metros cúbicos: "))

c = agua(mes, ano, consumo)
calc = c.calc_agua()
print(f"a conta de água de {mes} de {ano} teve o valor de {calc}")
