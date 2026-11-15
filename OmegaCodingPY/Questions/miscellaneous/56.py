''''
 Removal all characters from a string except integers
Given:

str1 = 'I am 25 years and 10 months old'
Expected Output:

2510
'''

str1 = 'I am 25 years and 10 months old'
str2 = ""
for char in str1:
    if char.isnumeric():
        str2 += char

str1 = str2
print(str1)