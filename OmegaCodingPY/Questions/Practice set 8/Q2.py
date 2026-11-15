# Write a class “Calculator” capable of finding square, cube and square root of a 
# number.
import math

class Calculator:
    def __init__(self,square,cube,square_root):
        self.square = square
        self.cube = cube
        self.square_root = square_root

n = int(input("Enter the number : "))

n = Calculator(n**2,n**3,math.sqrt(n))

print(n.square,n.cube,n.square_root)