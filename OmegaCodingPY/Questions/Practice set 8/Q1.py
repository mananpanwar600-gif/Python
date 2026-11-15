# Create a class “Programmer” for storing information of few programmers 
# working at Microsoft. 

class Programmer:
    company = "Microsoft"
    
    def __init__(self,name,language,salary):
        self.name = name
        self.language = language
        self.salary = salary

P1 = Programmer("MSP","Python",3000000)
P2 = Programmer("Ravi","C#",2300000)
P3 = Programmer("Joe","Node JS",2500000)

print(P1.name,P1.language,P1.salary,P1.company)
print(P2.name,P2.language,P2.salary,P2.company)
print(P3.name,P3.language,P3.salary,P3.company)