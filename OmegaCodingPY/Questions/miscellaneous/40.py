'''
Create a string made of the first, middle and last character

Write a program to create a new string made of an input string’s first, middle, and last character.

Given:

str1 = "James"
Expected Output:

Jms
'''

str1 = "James"
L1 = list(str1)
L2 = []

mid = len(L1) // 2

L2.append(L1[0])
L2.append(L1[mid])
L2.append(L1[-1])

print("".join(L2))