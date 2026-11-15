''' 
Check Palindrome Number
Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.

Expected Output:

original number 121
Yes. given number is palindrome number

original number 125
No. given number is not palindrome number

'''
n = input("Enter number : ")
reverse = n[::-1]

if(n==reverse):
    print(f"{n} is Palindrome")
else:
    print(f"{n} is not Palindrome")