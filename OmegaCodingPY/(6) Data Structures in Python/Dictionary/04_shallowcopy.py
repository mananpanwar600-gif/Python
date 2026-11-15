student = {"name": "MSP","age": 19,"Grade": 'O'}

# student_copy = student
# print(student_copy)

# student["name"] = "MSP1"
# print(student_copy)


''' USING SHALLOW COPY'''

student_copy = student.copy()
print(student_copy)

student["name"] = "MSP2"
print(student_copy)