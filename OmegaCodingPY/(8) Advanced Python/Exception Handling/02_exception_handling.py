try:
    num = int(input("Enter the number : "))
    result = 10/num
    print(result)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)