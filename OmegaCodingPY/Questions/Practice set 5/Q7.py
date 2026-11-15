#  If the names of 2 friends are same; what will happen to the program in problem 
# 6? 

#  If languages of two friends are same; what will happen to the program in problem 
# 6?

''' It will be printed only one time as dictionary does not contain dupicate keys but its not necessary for values to be unique'''

dict = {}

for i in range(4):
    names = input(f"Enter name of friend {i+1} : ").lower()
    lang = input(f"Enter language of friend {i+1} : ").lower()
    dict.update({names:lang})


print(dict)
