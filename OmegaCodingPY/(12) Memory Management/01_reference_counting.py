'''
Python uses reference counting to manage memory. Each object keeps track of how many references point to it. When the reference count drops to zero i.e., no references remain, Python automatically deallocates the object.
'''

import sys

a = []

## 2 (one ref is from 'a' and one from getrefcount())
print(sys.getrefcount(a))

b=a
print(sys.getrefcount(a))
del b
print(sys.getrefcount(a))



