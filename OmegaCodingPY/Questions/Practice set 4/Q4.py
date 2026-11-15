#  Write a program to sum a list with 4 numbers. 

def add(lst, n):
    if n == 0:
        return lst[0]
    return lst[n] + add(lst, n - 1)

lst = [int(input("Enter data : ")) for i in range(4)]

result = add(lst, 3)
print(result)