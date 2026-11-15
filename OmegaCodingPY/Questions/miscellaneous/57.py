'''
Find words with both alphabets and numbers
Write a program to find words with both alphabets and numbers from an input string.

Given:

str1 = "Emma25 is Data scientist50 and AI Expert"
Expected Output:

Emma25
scientist50
'''

str1 = "Emma25 is Data scientist50 and AI Expert"
temp = str1.split()

for char in temp:
    if not char.isalpha():
        print(char)