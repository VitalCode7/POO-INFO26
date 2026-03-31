class Pais:
    def __init__(self, nome, populacao, area):
        self.nome = nome
        self.populacao = populacao
        self.area = area

    def dens(self):
        return self.populacao / self.area

paises = []

for i in range(10):
    nome = input("Digite o nome do país: ")
    populacao = int(input("Digite sua população: "))
    area = float(input("Digite a área em km2: "))
    p = Pais(nome, populacao, area)
    paises.append(p)

maior = max(paises, key=lambda p: p.dens())

print("País com maior densidade:", maior.nome)
print("Densidade:", maior.dens())