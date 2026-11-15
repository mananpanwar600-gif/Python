'''
Check if a user-entered string contains any digits using a for loop
Expected Output:

Enter a string: Pynative123Python
The string contains at least one digit.

Enter a string: PYnative
The string does not contain any digits.
'''

def contains_digits(text):
  
  for char in text:
    if '0' <= char <= '9':
      return True  
  return False 

user_string = input("Enter a string: ")

print(contains_digits(user_string))
