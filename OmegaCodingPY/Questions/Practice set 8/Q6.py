# Can you change the self-parameter inside a class to something else (say 
# “MSP”). Try changing self to “slf” or “MSP” and see the effects.

'''WE CAN SELF WORKS AS A NAME AND WE CAN HAVE ANY NAME INPLACE OF SELF BUT USUALLY SELF IS USED AND IS MANDATORY'''

class Programmer:
    company = "Microsoft"
    
    def __init__(MSP,name,language,salary):
        MSP.name = name
        MSP.language = language
        MSP.salary = salary

P1 = Programmer("Raju","Python",3000000)
P2 = Programmer("Ravi","C#",2300000)
P3 = Programmer("Joe","Node JS",2500000)

print(P1.name,P1.language,P1.salary,P1.company)
print(P2.name,P2.language,P2.salary,P2.company)
print(P3.name,P3.language,P3.salary,P3.company)