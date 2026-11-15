'''
 Count the total number of digits in a number
Write a Python program to count the total number of digits in a number using a while loop.

For example, the number is 75869, so the output should be 5.
'''

n = int(input("Enter the number : "))

count = 0
ld = 0 
while(n!=0):
    ld = n%10
    n = n//10
    count = count + 1
print(count)