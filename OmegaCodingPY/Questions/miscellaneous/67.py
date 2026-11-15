'''
Create a copy of a list
Create a copy of a list [10, 20, 30] and modify the copy. Print both the original and the copied list to demonstrate they are independent.
'''

l = [10,20,30]

l1 = l.copy()
print(l1)

l.append(40)
print(l)
print(l1)