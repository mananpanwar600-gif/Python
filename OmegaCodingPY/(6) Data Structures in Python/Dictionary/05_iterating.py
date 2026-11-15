##You can use loops to iterate over dic,keys,values, or items

student = {"name": "MSP","age": 19,"Grade": 'O'}

for keys in student.keys():
    print(keys)

print('\n')

for values in student.values():
    print(values)

print('\n')

for key,value in student.items():
    print(f"{key}: {value}")

print('\n')

