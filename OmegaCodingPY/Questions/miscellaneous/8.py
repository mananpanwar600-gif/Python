'''
Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''
n = int(input("Enter the number : "))
t = 1
for i in range(n):
    print(f"{t}" * (i+1))
    t = t + 1