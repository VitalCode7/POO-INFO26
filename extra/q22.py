d = 5
s = 1
for k in range(28):
    if k % d == 0: print(s * k, end = ", ")
s = -s

# class Retangulo:
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura
#     def diagonal(self):
#         diago = (self.base**2 + self.altura**2)**(1/2)
#         return diago
# base = float(input())
# altura = float(input())
# r = Retangulo(base,altura)
# d = r.diagonal()
# print(d)

# class Retangulo:
#     def __init__(self):
#         self.base = 0
#         self.altura = 0
#     def diagonal(self):
#         return ((self.base**2) + (self.altura**2))(**1/2)

# x = Retangulo()
# x.base = float(input())
# x.altura = float(input())
# print(x.diagonal()) 

import math

class Retangulo: 
    def __init__(self):
        self.base = 0
        self.altura = 0
        
    def diagonal(self):
        # Usamos parênteses extras para garantir que a raiz quadrada (1/2) 
        # seja aplicada ao resultado da soma, e não apenas ao último termo.
        return (self.base**2 + self.altura**2)**(1/2)

# 1. Instanciação: Use parênteses para criar um objeto da classe
x = Retangulo() 

x.base = float(input("Digite a base: "))
x.altura = float(input("Digite a altura: "))

# 2. Chamada de método: Use parênteses para executar a função
print(f"A diagonal é: {x.diagonal()}")