class Person:
    def __init__(self,name,age):
        self.name = name ##public variable
        self.age = age #Public variable   
person = Person("MSP",19)
print(dir(person))