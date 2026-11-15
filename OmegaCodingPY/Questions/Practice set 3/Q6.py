#  Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50        
# => F 

marks = [int(input(f"Enter marks of subject {i+1} : ")) for i in range(5)]
sum = 0
for i in range(5):
    sum += marks[i]

avg = sum/5

if avg>=90 and avg<=100:
    print("O")

elif avg>=80 and avg<90:
    print("A")

elif avg>=70 and avg<80:
    print("B")

elif avg>=60 and avg<70:
    print("C")

elif avg>=50 and avg<60:
    print("D")

else:
    print("F")