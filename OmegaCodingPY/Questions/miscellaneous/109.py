'''
Define a property that must have the same value for every class instance (object)
Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

Use the following code for this exercise.

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

Expected Output:

Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18
'''

class Vehicle:
    color = "White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

bus = Bus("School Volvo",180,12)
print(bus.color,bus.name,bus.max_speed,bus.mileage)
car = Car("Audi Q5",240,18)
print(car.color,car.name,car.max_speed,car.mileage)
