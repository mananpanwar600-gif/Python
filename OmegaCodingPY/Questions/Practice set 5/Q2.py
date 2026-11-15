#  Write a program to input eight numbers from the user and display all the unique 
# numbers (once). 

numbers = [input("Enter number : ") for i in range(8)]
unique_numbers = set(numbers)
print(numbers)
print(unique_numbers)