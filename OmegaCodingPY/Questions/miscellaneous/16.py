'''
Generate Fibonacci series up to 15 terms
Have you ever wondered about the Fibonacci Sequence? It’s a series of numbers in which the next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.

For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series is 13 + 21 = 34.

Expected output:

Fibonacci sequence:
0  1  1  2  3  5  8  13  21  34  55  89  144  233  377
'''

'''
Generate Fibonacci series up to 15 terms
Have you ever wondered about the Fibonacci Sequence? It’s a series of numbers in which the next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.

For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series is 13 + 21 = 34.

Expected output:

Fibonacci sequence:
0  1  1  2  3  5  8  13  21  34  55  89  144  233  377
'''

n = int(input("Enter nth term : "))
a = 0
b = 1

print(a,b,end=" ")
for i in range(n-2):
    c = a+b
    print(c, end="  ")
    a = b
    b = c