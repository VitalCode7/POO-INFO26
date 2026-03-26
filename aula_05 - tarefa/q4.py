frase = input("digite uma frase: ")
l = frase.split(",")
soma = 0
x = 0
while x < len(l):
    soma += int(l[x])
    x += 1
print(soma)