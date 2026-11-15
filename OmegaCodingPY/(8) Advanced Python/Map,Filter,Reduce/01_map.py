def square(x):
        return x**2
    
numbers = [1,2,3,4,5]
squared_numbers = list(map(square,numbers))
print(squared_numbers)

#Using List Comp.
squared_numbers_lc = [x**2 for x in numbers]
print(squared_numbers_lc)