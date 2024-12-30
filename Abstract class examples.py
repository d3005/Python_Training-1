from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass
class SuzukiCar(Car):
    def mileage(self):
        print("The Mileage is 20kmph")
class TeslaCar(Car):
    def mileage(self):
        print("The Mileage is 30kmph")
s1=SuzukiCar()
t1=TeslaCar()
s1.mileage()
t1.mileage()
c1=Car()
c1.mileage()