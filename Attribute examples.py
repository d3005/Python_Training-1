"""class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
p1=Person("John", "Smith")
print(getattr(p1,"first_name"))
print(getattr(p1,"last_name"))
setattr(Person, "first_name", "Jos")
print(getattr(p1,"first_name"))
print(getattr(p1,"last_name"))
print(hasattr(p1,"first_name"))
print(hasattr(p1,"name"))"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("John",29)
print(getattr(p1,"name"))
print(getattr(p1,"age"))
setattr(p1,"name","Jos")
print(getattr(p1,"name"))
print(getattr(p1,"age"))
print(hasattr(p1,"age"))
print(hasattr(p1,"id"))