#  Write a program which finds out whether a given name is present in a list or not.

name = ["Arjun","Sameer","Parth","Gulia","Jack"]
given_name = input("Enter the name : ").capitalize()

if given_name in name:
    print("CONGO, NAME FOUND")
else:
    print("SORRY!! :(")