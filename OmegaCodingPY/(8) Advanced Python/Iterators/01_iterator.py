my_list = [1,2,3,4,5,6]

##Iterator

iterator = iter(my_list)

##Lazy loading

try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print("There are no elements in the iterator")

##More effective in jupyter notebook