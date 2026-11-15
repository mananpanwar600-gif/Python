class Person:
    def __init__(self,name,age):
        self._name = name ##protected variable
        self._age = age #protected variable   
class Employee(Person):
    def __init__(self,name,age):
        super().__init__(name,age)

def get_name(person):
    return person.__name

employee = Employee("MSP",19)
print(employee._name)

#Protected variables can be accessed from derived class