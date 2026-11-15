'''
Symmetric Difference
Find the symmetric difference of set1 and set2. Write a code to returns a new set containing elements that are unique to either set1 or set2, but not in both. It’s like finding the union and then removing the intersection.

Given:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
'''

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

#A Δ B = (A ∪ B) - (A ∩ B)

print(set1.symmetric_difference(set2))
print(set1^set2)

print((set1|set2)-(set1&set2))