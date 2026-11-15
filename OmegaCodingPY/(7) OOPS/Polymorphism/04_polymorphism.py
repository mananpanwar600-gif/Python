#Polymorphism with abstract base classes

from abc import ABC,abstractmethod

##Define a abstract class

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"
    
def start_vehicle(vehicle):
    print(vehicle.start_engine())
    
car = Car()
motorcycle = Motorcycle()

start_vehicle(car)
start_vehicle(motorcycle)
