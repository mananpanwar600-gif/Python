#Class is a blueprint or template 
#Specific instance created from template(class) is called Object

class Employee:
    company = "HP"

    def get_salary(self):    #self is imp as self is the way of reference the object of class which has been created
        return 34000
    
e = Employee()          #AN OBJECT OF CLASS EMPLOYEE IS CREATED HERE
print(e.get_salary()) 