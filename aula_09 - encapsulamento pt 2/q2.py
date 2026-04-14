class Viagem:
    def __init__(self):
        self.__distancia = 0
        self.__tempo = 0
    def set_distancia(self, d):
        if d <= 0: raise ValueError("Valor inválido, digite um número positivo")
        self.__distancia = d
    def set_tempo(self, t):
        if t <= 0: raise ValueError("Valor inválido, digite um número positivo")
        self.__tempo = t
    def get_distancia(self):
        return self.__distancia
    def get_tempo(self):
        return self.__tempo
    def velocidade_media(self):
        return self.__distancia / self.__tempo