'''
Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

Expected Output:

The seating capacity of a bus is 50 passengers
'''

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        return f"The seating capacity of {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity):  # Set default value here
        return super().seating_capacity(capacity)
    
School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity(50))