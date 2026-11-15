# . Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * *  

n = int(input("Enter n : "))

for i in range(n):
    if i == 0 or i == n - 1:
        print('* ' * n)
    else:
        print('*' + ' ' * (2 * n - 3) + '*')