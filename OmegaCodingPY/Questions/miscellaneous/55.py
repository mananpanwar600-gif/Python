'''
Remove special symbols / punctuation from a string
Given:

str1 = "/*Jon is @developer & musician"
Expected Output:

"Jon is developer musician"
'''

str1 = "/*Jon is @developer & musician"
str2=""

for char in str1:
    if char.isalnum() or char.isspace():
        str2 += char
str1 = str2
print(str1)

##OR

# import re

# str1 = "/*Jon is @developer & musician"
# print("Original string is ", str1)

# res = re.sub(r'[^\w\s]', '', str1)
# print("New string is ", res)