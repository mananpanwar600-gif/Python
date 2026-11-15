number = [1,2,3,4,5,6,7,8,9,10]

even = list(filter(lambda x : x%2==0,number))
print(even)

# even_lc = [x for x in number if x%2==0]
# print(even)

odd = list(filter(lambda x : x%2!=0,number))
print(odd)

# odd_lc = [x for x in number if x%2!=0]
# print(odd)