marks = [54,23,64,93,32]
mixed = [43,"Hello",False,4.22]

print(marks)
print(mixed)

print(marks[2])
print(mixed[1])

marks[2] = 90     #List are mutable
mixed[1] = "KSP"

print(marks[2])
print(mixed[1])

print(marks[2:4])  #Slicing same as string