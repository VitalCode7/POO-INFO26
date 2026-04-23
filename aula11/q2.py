class Frete:
    def __init__(self, d, p):
        self.__distancia = 0
        self.__peso = 0
        self.set_distancia(d) 
        self.set_peso(p) 
    
    def set_distancia(self, v):
        if v >= 0: self.__distancia = v
        else: raise ValueError()
    
    def set_peso(self, v):
        if v >= 0: self.__peso = v
        else: raise ValueError()
    
    def get_distancia(self):
        return self.__distancia
    
    def get_peso(self):
        return self.__peso

    def calc_frete(self):
        return self.__distancia * self.peso / 100
    
    def __str__(self):
        return f"Distancia = {self.__distancia} - Peso = {self.__peso}"