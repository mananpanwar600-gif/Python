##Can be done with Getter and Setter methods

class Person:
    def __init__(self,name,age):
        self.__name = name #Private access modifier
        self.__age = age
    
    ##getter method for name
    def get_name(self):
        return self.__name

    ##setter method for name
    def set_name(self,name):
        self.__name = name

    ##getter method for age
    def get_age(self):
        return self.__age

    ##setter method for age
    def set_age(self,age):
        if age>0:
            self.__age = age
        else:
            print("Age can't be -ve.")


person = Person("MSP",19)

##Access and modify private variables using getter and setter

print(person.get_name())
print(person.get_age())

person.set_name("POPPY")
person.set_age(15)

print(person.get_name())
print(person.get_age())