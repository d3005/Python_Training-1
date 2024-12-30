#Single Level Inheritance
"""
class Father:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(self.name)
class Son(Father):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
    def show1(self):
        print(self.name)
x = Father('Anil')
x.show()
y=Son('Akhil')
y.show1()
y.show()
class Base:
    def __init__(self):
        self._a=18
class derived(Base):
    def __init__(self):
        Base.__init__(self)
        print(self._a)
d1=derived()
b1=Base()
print(b1._a)"""
#Multi-Level Inheritance
'''class Base:
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
d=derive1()'''
#Multiple Inheritance
'''class father:
    fathername=''
    def Father(self):
        print(self.fathername)
class mother:
    mothername=''
    def Mother(self):
        print(self.mothername)
class son(father,mother):
    name=''
    def show(self):
        print(self.fathername)
        print(self.mothername)
        print(self.name)
s1=son()
s1.name="LAVA"
s1.fathername="Ram"
s1.mothername="seetha"
s1.show()
s1.Father()
s1.Mother()'''
#Hierarchical Inheritance
'''class father:
    fathername=''
    def Father(self):
        print(self.fathername)
class mother:
    mothername=''
    def Mother(self):
        print(self.mothername)
class son(father,mother):
    name=''
    def show(self):
        print(self.fathername)
        print(self.mothername)
        print(self.name)
class son1(father):
    name=''
    def show1(self):
        print(self.fathername)
        print(self.name)
s2=son1()
s2.name="Akhil"
s2.fathername="ram"
s2.show1()
s2.Father()'''
#Hybrid Inheritance
class father:
    fathername=''
    def Father(self):
        print(self.fathername)
class mother:
    mothername=''
    def Mother(self):
        print(self.mothername)
class son(father,mother):
    name=''
    def show(self):
        print(self.fathername)
        print(self.mothername)
        print(self.name)
class son1(father):
    name=''
    def show1(self):
        print(self.fathername)
        print(self.name)
s1=son()
s1.name="LAVA"
s1.fathername="Ram"
s1.mothername="seetha"
s1.show()
s1.Father()
s1.Mother()
s2=son1()
s2.name="Akhil"
s2.fathername="ram"
s2.show1()
s2.Father()
#issubclass()
class cal1:
    def sum(self,a,b):
        return a+b
class cal2:
    def mul(self,a,b):
        return a*b
class call(cal1,cal2):
    def div(self,a,b):
        return a/b
d=call()
print(d.sum(1,3))
print(issubclass(call,cal1))
print(issubclass(call,cal2))
print(issubclass(cal1,cal2))
print(isinstance(d,cal1))
print(isinstance(d,cal2))
print(isinstance(d,cal1))