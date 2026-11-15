#  Write a program to fill in a letter template given below with name and date. 
# letter = '''  
# Dear <|Name|>, 
# You are selected! 
# <|Date|> 
# ''' 

letter = '''  
Dear {}, 
You are selected!
{} 
''' 

a = "Harry"
a1 = "12/12/2025"

b = "Shubham"
b1 = "1/01/2026"

print(letter.format(a,a1))
print(letter.format(b,b1))