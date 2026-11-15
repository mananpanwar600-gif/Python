'''
 Calculate the sum and average of the digits present in a string
Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

Given:

str1 = "PYnative29@#8496"
'''
def sum_avg(str1):
    sum = 0
    count = 0
    for digit in str1:
        if digit.isnumeric():
            p = int(digit)
            sum = sum+p
            count +=1
    avg = sum/count

    return sum,avg

str1 = "PYnative29@#8496"
print(f"The sum and avg of numbers in string are : {sum_avg(str1)}")