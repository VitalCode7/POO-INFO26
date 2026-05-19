from datetime import datetime, timedelta

nasc = datetime.strptime(input("Informe a data de nascimento: "), "%d/%m/%Y")
hoje = datetime.now()
idade = hoje - nasc
print(idade)
anos = idade.days//365
print(anos, "anos")
meses = idade.days % 365 // 30
print(meses, "meses")
dias = idade.days % 30
print(dias, "dias")