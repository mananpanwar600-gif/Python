'''
Remove and add item in a list

Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

Given:

sample_list = [34, 54, 67, 89, 11, 43, 94]
Expected Output:

List After removing element at index 4  [34, 54, 67, 89, 43, 94]
List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]
'''

sample_list = [34, 54, 67, 89, 11, 43, 94]
sample_list.pop(4)
print(sample_list)
sample_list.insert(2,11)
print(sample_list)
sample_list.append(11)
print(sample_list)