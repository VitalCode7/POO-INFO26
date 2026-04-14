class Ingresso:
    def __init__(self, dia, hora, meia):
        self.__dia = dia
        self.__hora = hora
        self.__meia = meia
        self.__valor = 0

    def set_dia(self, d):
        self.__dia = d
        
    def set_hora(self, h):
        self.__hora = h
    
    def set_meia(self, m):
        self.__meia = m
    
    def get_dia(self):
        return self.__dia
    
    def get_hora(self):
        return self.__hora
    
    def get_meia(self):
        return self.__meia
    
    def get_valor(self):
        return self.__valor
    
    def calc(self):

        if self.__dia == 4:
            self.__valor = 8
            return self.__valor

        elif self.__dia in [2, 3]:
            self.__valor = 16

        else:
            self.__valor = 20

        if self.__hora >= 17:
            self.__valor *= 1.5

        if self.__meia == 's':
            self.__valor /= 2

        return self.__valor


x = Ingresso(2,18,'s')
v = x.calc()
print(f"O valor do ingresso é R${v:.2f}")
