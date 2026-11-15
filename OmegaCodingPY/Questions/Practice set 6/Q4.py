#  Write a program to find whether a given number is prime or not.

n = int(input("Enter the number : "))

if(n<=1):
   print(f"{n} is not prime")
else:
    flag = True
    for i in range(2,n-1):
        if n%i==0:
            flag = False

    if flag:
        print(f"{n} is Prime")
    else:
        print(f"{n} is not Prime")