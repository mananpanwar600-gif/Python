# Write a program to find whether a given username contains less than 10 
# characters or not. 

name = input("Enter username : ").lower()

if len(name)<10:
    print("USERNAME HAS LESS THAN 10 CHARACTERS")
else:
    print("VALID")