import math
class circulo:
    def __init__(self):
        self.r = 0
    def calc_area(self):
        return math.pi * (self.r**2)
    def calc_circun(self):
        return 2 * self.r * math.pi
x = circulo()
x.r = float(input())
a = x.calc_area()
c = x.calc_circun()
print(f"área: {a}, circunferência: {c}")