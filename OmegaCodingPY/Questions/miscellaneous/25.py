''''
Calculate sum of all numbers from 1 to a given number
Write a Python program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

For example, if the user entered 10, the output should be 55 (1+2+3+4+5+6+7+8+9+10)

Expected Output:

Enter number 10
Sum is:  55
'''

n = int(input("Enter the nth term : "))
sum = 0
for i in range(1,n+1):
    sum = sum + i

print(sum)