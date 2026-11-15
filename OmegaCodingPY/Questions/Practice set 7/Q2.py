#  Write a python program using function to convert Celsius to Fahrenheit. 

def C_to_F(c):
    F = (c * (9/5)) + 32
    return F

c = int(input("Enter the temp in degree celsius : "))

print(f"{c} degree in fahrenheit is {C_to_F(c)}")