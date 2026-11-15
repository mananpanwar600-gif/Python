'''
Create a new string made of the first, middle, and last characters of each input string
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

Given:

s1 = "America"
s2 = "Japan"
Expected Output:

AJrpan
'''
def middle_term(s):
    mid = len(s)//2
    return mid

def end_term(s):
    end = len(s) - 1
    return end

def new_string(s1,s2):
    first_char = s1[0] + s2[0]
    second_char = s1[middle_term(s1)]+s2[middle_term(s2)]
    third_char = s1[end_term(s1)] + s2[end_term(s2)]

    s3 = first_char+second_char+third_char
    return s3

s1 = "America"
s2 = "Japan"

print(new_string(s1,s2))