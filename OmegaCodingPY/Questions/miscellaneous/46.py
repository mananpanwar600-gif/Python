'''
 Arrange string characters such that lowercase letters should come first
Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

Given:

str1 = PyNaTive
Expected Output:

yaivePNT
'''
def arrange(str1):
    lower = []
    upper = []
    for char in str1:
        if(char.islower()):
            lower.append(char)
        if(char.isupper()):
            upper.append(char)

    str2 = "".join(lower + upper)
    return str2

str1 = "PyNaTive"
print(arrange(str1))