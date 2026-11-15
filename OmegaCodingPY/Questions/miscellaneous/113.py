'''
 Check object is a subclass of a particular class
Given:

class Animal:
    pass

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

class Cat:
    pass
Write a code to check the following

Dog is a subclass of Animal? –> True
Animal is a subclass of Dog? –> False
Cat is a subclass of Animal? –> False
Puppy is a subclass of Animal –> True
'''

class Animal:
    pass

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

class Cat:
    pass

print(f"Dog is a subclass of Animal?   -> {issubclass(Dog,Animal)}")
print(f"Animal is a subclass of Dog?   -> {issubclass(Animal,Dog)}")
print(f"Cat is a subclass of Animal?   -> {issubclass(Cat,Animal)}")
print(f"Puppy is a subclass of Animal? -> {issubclass(Puppy,Animal)}")