# Write a program to print multiplication table of n using for loops in reversed 
# order.

n = int(input("Enter the number : "))

for i in range(10,0,-1):
    table = n*i
    print(f"{n}X{i} = {table}")