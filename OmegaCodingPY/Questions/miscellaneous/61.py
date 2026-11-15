'''
Sum and average of all numbers in a list
Calculate and print the sum and average of all numbers in a list.

Given:

my_list = [10, 20, 30, 40, 50]
Expected Output:

Sum: 150
Average: 30.0
'''

my_list = [10,20,30,40,50]
sum = 0
for item in my_list:
    sum += item

print("Sum:",sum)
print("Average:",sum/len(my_list))