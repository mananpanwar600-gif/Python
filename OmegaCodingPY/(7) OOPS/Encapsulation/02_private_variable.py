class Person:
    def __init__(self,name,age):
        self.__name = name ##private variable
        self.__age = age #private variable   

def get_name(person):
    return person.__name

person = Person("MSP",19)
print(get_name(Person))
# print(dir(person))

#Private variable cannot be accessed outside the class thus we use getters and setters