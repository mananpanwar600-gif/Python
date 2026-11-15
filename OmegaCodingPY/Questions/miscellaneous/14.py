'''
Print a downward half-pyramid pattern of stars
* * * * *  
* * * *  
* * *  
* *  
*

'''
n = int(input("Enter n : "))
for i in range(n):
    print("*" * (n-i))