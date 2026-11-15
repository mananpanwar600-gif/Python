'''
 Print the following pattern
Write a program to print the following start pattern using the for loop

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*                                                                                                 
'''

n = int(input("Enter n : "))

for i in range(n):
    print("* " * (i+1))

for i in range(n):
    print("* " * (n-i-1))