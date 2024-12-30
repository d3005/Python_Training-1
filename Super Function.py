class Base:
    def __init__(self):
        self.a=26
        print(self.a)
class derive(Base):
    def __init__(self):
        Base.__init__(self)
        print(self.a+2)

class derive1(derive):
    def __init__(self):
        derive.__init__(self)
        print(self.a+3)

d=derive1()