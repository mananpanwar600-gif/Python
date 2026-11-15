class Employee:
    company = "ASUS"  #Class Attribute

    def __init__(self,salary,name,bond,company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary

    def getInfo(self):
        print(f"The name of employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")

e1 = Employee(34000,"John Doe",4,"Tesla")
print(e1.company)  #This will print instance attribute if present

print(Employee.company) #The class attribute will be printed