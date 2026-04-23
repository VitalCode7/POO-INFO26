class E2:
    def __init__(self, a, b, c):
        self.__a = 0
        self.__b = 0
        self.__c = 0
        self.delta = 0
        self.set_a(a) 
        self.set_b(b) 
        self.set_c(c)

    def set_a(self, v):
        if v >= 0 : self.__a = v
    
    def set_b(self, v):
        if v >= 0 : self.__b = v
    
    def set_c(self, v):
        if v >= 0 : self.__c = v
    
    def get_a(self):
        return self.__a
    
    def get_b(self):
        return self.__b
    
    def get_c(self):
        return self.__c

    def delta(self):
        self.delta = (self.__b ** 2) - (4 * self.__a * self.__c)
    
    def TemRaizesReais:
        if self.delta < 0: return False
        else: return True