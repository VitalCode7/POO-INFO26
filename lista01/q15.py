def primo(n):
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
    if primo == True:
        print(f"{n} é primo")
    else:
        print(f"{n} Não é primo")
primo(3)
primo(2)
primo(4)
primo(7)
primo(9)
primo(11)
primo(13)
primo(15)