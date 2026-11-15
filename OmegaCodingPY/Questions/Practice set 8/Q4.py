#  Add a static method in problem 2, to greet the user with hello. 

import math

class Calculator:
    def __init__(self,square,cube,square_root):
        self.square = square
        self.cube = cube
        self.square_root = square_root

    def greet(self):
        print("Hello")
    

n = int(input("Enter the number : "))

n = Calculator(n**2,n**3,math.sqrt(n))

n.greet()
print(n.square,n.cube,n.square_root)
