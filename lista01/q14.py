lista = []
def mmc(x,y):
    if x > y:
        for i in range(2, y + 1):
            if x % i == 0 and y % i == 0:
                lista.append(i)
    else:
        for i in range (2, x + 1):
            if x % i == 0 and y % i == 0:
                lista.append(i)
    print(f"{lista[0]}")
mmc(81, 27)