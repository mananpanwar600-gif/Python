'''
Write a Python code to display numbers from a list divisible by 5

Expected Output:

Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55
'''

list = [10,20,33,46,55]

for i in list:
    if i%5==0:
        print(i)