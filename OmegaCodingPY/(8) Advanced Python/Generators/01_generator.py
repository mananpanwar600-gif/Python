##Simpler way to create the iterator

def square(n):
    for i in range(3):
        yield i**2
    
    
for i in square(3):
    print(i)

##OR
a = square(3)

print(next(a))
print(next(a))