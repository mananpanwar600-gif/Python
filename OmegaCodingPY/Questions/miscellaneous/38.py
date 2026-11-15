'''' ***********IMPORTANT*****************
Flatten a nested list using loops
Write a program to flatten a nested list using loops.

Given:

nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]

# write function 'flatten_list' to flatten a nested list
flattened = flatten_list(nested_list)
print("Flattened list:", flattened)

# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
def flatten_list(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element,list):  #isinstance used for checking subclass 
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list


nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]

flattened = flatten_list(nested_list)
print("Flattened list:", flattened)

