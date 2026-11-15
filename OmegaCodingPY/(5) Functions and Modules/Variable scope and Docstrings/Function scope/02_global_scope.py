def sum(a,b):
    # a and b are local variables
    c = a+b
    z=1             # It creates a local variable which destroyed after function returns
    return c



z=8  #z is global variable
print(sum(4,6))
print(z) 