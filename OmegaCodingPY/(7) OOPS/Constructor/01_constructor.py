class Employee:
    
    def __init__(self,salary,name,bond):
        self.salary = salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary

    def getInfo(self):
        print(f"The name of employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")

e1 = Employee(34000,"John Doe",4)
e1.getInfo()