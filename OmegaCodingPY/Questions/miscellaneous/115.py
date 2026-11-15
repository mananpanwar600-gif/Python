''''
 List Creation using two lists
Write a code to create a new list using odd-indexed elements from the first list and even-indexed elements from the second

Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.

Given:

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
Expected Output:

Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]

Printing Final third list
[6, 12, 18, 4, 12, 20, 28]

'''

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = []

l1 = [l1[i] for i in range(len(l1)) if i%2!=0]
print(f"Element at odd index position from list one\n{l1}")

l2 = [l2[i] for i in range(len(l2)) if i%2==0]
print(f"Element at odd index position from list one\n{l2}")

for i,j in zip(l1,l2):
    l3.append(i)
    l3.append(j)

print(f"Printing Final third list\n{l3}")