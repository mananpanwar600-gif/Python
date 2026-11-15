students={
    "student1":{"name":"MSP","age":19},
    "student2":{"name":"Peter","age":35}
}

print(students)

##Accessing

print(students["student2"]["name"])
print(students["student2"]["age"])

##iterating

for student_id,student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key,value in student_info.items():
        print(f"{key}:{value}")
