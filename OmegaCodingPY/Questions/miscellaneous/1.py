'''You're given three integers (x, y, z) that define the size of a 3D grid (like the dimensions of a cuboid). You're also given a fourth integer n.

You need to generate all possible coordinate combinations [i, j, k] where:

0 ≤ i ≤ x

0 ≤ j ≤ y

0 ≤ k ≤ z

BUT — you should exclude any coordinate where the sum i + j + k == n.

Use list comprehension (not regular loops) to build and print the list of these valid coordinates in lexicographic (default Python) order. '''


x = int(input("Enter x : "))
y = int(input("Enter y : "))
z = int(input("Enter z : "))
n = int(input("Enter n : "))
    
list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
    
print(list)
    