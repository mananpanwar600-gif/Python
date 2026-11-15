'''
Find largest and smallest digit in a number
Write a program in Python identifies the digit with the highest value and the digit with the lowest value within that number.

Input:

num1 = 9876543210
num2 = -5082
Output:


Largest digit in 9876543210: 9
Smallest digit in 9876543210: 0

Largest digit in -5082: 8
Smallest digit in -5082: 0
'''

n = int(input("Enter the number : "))
print(f"Largest digit in {n} : {max(str(n))}")
t = abs(n)           #Inbuilt function which finds absolute value
print(f"Largest digit in {n} : {min(str(t))}")

