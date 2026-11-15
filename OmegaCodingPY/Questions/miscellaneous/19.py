'''
Print Reverse Number Pattern
Expected Output:

1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 
'''
n = int(input("Enter n : "))
t = 1
for i in range(n):
    print(f"{t}" * (n-i))
    t = t+1