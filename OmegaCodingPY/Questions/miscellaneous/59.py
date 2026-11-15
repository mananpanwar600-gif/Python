''''
 Perform Basic List Operations
Given:

my_list = [10, 20, 30, 40, 50]
Perform following operations on given list

Access Elements: Print the third element.
List Length: Print the number of elements in the list
Check if Empty: Write a code to check is list empty.
Expected Output:

Initial list: [10, 20, 30, 40, 50]

Third item:  30
Length of the list: 5
list is not empty
'''

l = [10,20,30,40,50]

print(l[2])
print(len(l))

if len(l) == 0:
    print("List is Empty")
else:
    print("List is not empty")