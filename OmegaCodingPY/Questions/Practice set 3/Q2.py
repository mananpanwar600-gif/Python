# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
#  take marks as an input from the user.

maths = int(input("Enter marks in maths : "))
phy = int(input("Enter the marks in physics : "))
chem = int (input("Enter the marks in chemistry : "))

total = (maths+phy+chem)/3

if(total>40):
    if(maths<33 or phy<33 or chem<33):
        print("FAILED")
    else:
        print("PASSED")

else:
    print("FAILED")