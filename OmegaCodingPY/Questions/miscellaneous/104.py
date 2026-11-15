'''
Check if all items in the tuple are the same
tuple1 = (45, 45, 45, 45)
'''
def check(tuple1):
    return all(i == tuple1[0] for i in tuple1)

tuple1 = (45, 45, 45, 45)
print(check(tuple1))