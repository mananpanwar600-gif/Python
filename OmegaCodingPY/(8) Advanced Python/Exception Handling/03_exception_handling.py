# Alternative Method for 2nd program

try:
    num = int(input("Enter the number : "))
    result = 10/num
    print(result)
except(ZeroDivisionError,ValueError) as e:
    print(f"An error occured : {e}")