'''
Create a string made of the middle three characters
Write a program to create a new string made of the middle three characters of an input string.

Given:

Case 1

str1 = "JhonDipPeta"
Output

Dip
Case 2

str2 = "JaSonAy"
Output

Son
'''

string = input("Enter the string : ")
mid = len(string)//2

new_string = string[mid-1] + string[mid] + string[mid+1]

print(new_string)