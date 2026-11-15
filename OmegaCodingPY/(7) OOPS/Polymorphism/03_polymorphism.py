# Polymorphism with functions and methods 

class Shape:
    def area(self):
        return "The area of the figure"
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.width * self.length
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2
    
def print_area(shape):
    print(f"The area is {shape.area()}")


rectangle = Rectangle(4,5)
circle = Circle(3)

print_area(rectangle)
print_area(circle)