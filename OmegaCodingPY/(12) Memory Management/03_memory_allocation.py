'''
BEST PRACTICES FOR MEMEORY MANAGEMENT ARE::

1. Use Built-in Data Structures Wisely
2. Leverage List Comprehensions and Generator Expressions
3. Implement Context Managers for Resource Management
4. Use __slots__ for Memory-Sensitive Classes
5. Avoid Global Variables
6. Use Lazy Evaluation When Possible
7. Profile Your Code Regularly
'''

import gc
class MyObject:
    def __init__(self,name):
        self.name = name
        print(f"Object {self.name} created")

    def __del__(self):
        print(f"Object {self.name} is deleted")



## create circular refernce
obj1 = MyObject("obj1")
obj2 = MyObject("obj2")
obj1.ref = obj2
obj2.ref = obj1

del obj1
del obj2

## mannualy trigger the garbage collection

gc.collect()

print(gc.garbage)