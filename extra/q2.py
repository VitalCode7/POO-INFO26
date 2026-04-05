class Pessoa:
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def imc(self):
        return self.peso / (self.altura ** 2)


pessoas = []

for i in range(5):
    nome = input("Digite seu nome: ")
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    
    p = Pessoa(nome, peso, altura)
    pessoas.append(p)


maior = max(pessoas, key=lambda p: p.imc())

print(f"A pessoa com maior IMC é {maior.nome}")
