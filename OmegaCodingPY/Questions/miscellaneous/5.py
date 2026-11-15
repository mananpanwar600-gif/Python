''' 
Check if the first and last numbers of a list are the same
Write a code to return True if the list's first and last numbers are the same. If the numbers are different, return False.

Given:

numbers_x = [10, 20, 30, 40, 10]
# output True

numbers_y = [75, 65, 35, 75, 30]
# Output False
'''
lst = list(map(int, input("Enter the numbers in list : ").split()))

if lst[0] == lst[-1]:
    print("True")
else:
    print("False")


