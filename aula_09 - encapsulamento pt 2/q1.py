class Circulo:
    def __init__(self):
        self.__raio = 0
    def set_raio(self, v):
        if v < 0: raise ValueError("Valor inválido, digite um número positivo")
        self.__raio = v
    def get_raio(self):
        return self.__raio
    def calc_area(self):
        area = 3.14 * self.__raio ** 2
        return area
    def calc_circunferencia(self):
        circun = 2 * 3.14 * self.__raio
        return circun
   