class viagem:
    def __init__(self):
        self.km = 0
        self.hrs = 0
        self.mnt = 0
    def vm(self):
        return self.km/(self.hrs + (self.mnt/60))
x = viagem()
x.km = float(input())
x.hrs = float(input())
x.mnt = float(input())
v = x.vm()
print(v)