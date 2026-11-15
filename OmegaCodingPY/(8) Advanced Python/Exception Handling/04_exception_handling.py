#Using else and finally

a = int(input("Enter a : "))
b = int(input("Enter b : "))

try:
    r = a/b
except Exception as e:
    print(e)

else:
    print(r)

finally:
    print("Program has been executed.....")
