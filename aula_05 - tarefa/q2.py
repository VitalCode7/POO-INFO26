frase = input("digite uma frase: ")
for s in '+-*/':
    if s in frase:    
        l = frase.split(s)
        n1 = float(l[0])
        n2 = float(l[1])

        if s == '+':
            print(f'O resultado da operação é {n1 + n2}')
        elif s == '-':
            print(f'O resultado da operação é {n1 - n2}')
        elif s == '*':
            print(f'O resultado da operação é {n1 * n2}')
        elif s == '/':
            print(f'O resultado da operação é {n1 / n2}')       