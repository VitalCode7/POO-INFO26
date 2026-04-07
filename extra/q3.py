class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calc_a(self):
        area = self.base * self.altura
        return area
    def calc_p(self):
        peri = 2 * (self.base + self.altura)
        return peri
retangulos = []
for i in range(3):
    base = int(input("Digite o valor da base: "))
    altura = int(input("Digite o valor da altura: "))
    r = Retangulo(base, altura)
    retangulos.append(r)
maior = max(retangulos, key = lambda r: r.calc_a())
a = maior.calc_a()
print(f'A maior área entre os retangulos é {a}')