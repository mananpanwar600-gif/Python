'''
Set Intersection Check
Write a code to check if two sets have any elements in common. If yes, display the common elements


Given:

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
Expected output:

Two sets have items in common
{10}
'''
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

if set1.isdisjoint(set2):
    print("Set 1 and Set2 does not have any element in common")
else:

    print(f"Two sets have items in common\n{set1.intersection(set2)}")
