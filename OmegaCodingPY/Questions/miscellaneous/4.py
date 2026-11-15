'''
Write a Python code to accept a string from the user and display characters present at an even index number.

For example, str = "PYnative". so your code should display 'P', 'n', 't', 'v'.

Expected Output:

Orginal String is  PYnative
Printing only even index chars
P
n
t
v
'''

str = input("Enter the string : ")

i = 0
for i in range(0,len(str)):
    if(i%2==0):
        print(str[i])

