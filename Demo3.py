class cal:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        print("a + b = ",self.a + self.b)

    def sub(self):
        print("a - b = ",self.a - self.b)

    def mul(self):
        print("a * b = ",self.a * self.b)

    def div(self):
        print("a / b  = ",self.a / self.b)


obj = cal(10,5)
obj.add()
obj.sub()
obj.mul()
obj.div()