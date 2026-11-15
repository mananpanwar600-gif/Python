'''
Calculate the area of different shapes using OOP
Given:

You have given a Shape class and subclasses Circle  and Square. The parent class (Shape) has a area() method.


Now, Write a OOP code to calculate the area of each shapes (each subclass must write its own implementation of area() method to calculates its area).

Use the following code

class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented by subclasses")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

'''
from math import pi

class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented by subclasses")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side**2

shapes = [Circle(5),Square(3)]  #Poly morphism

for shape in shapes:
    print(shape.area())