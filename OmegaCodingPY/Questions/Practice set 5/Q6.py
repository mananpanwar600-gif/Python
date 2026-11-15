#  Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.

dict = {}

for i in range(4):
    names = input(f"Enter name of friend {i+1} : ").lower()
    lang = input(f"Enter language of friend {i+1} : ").lower()
    dict.update({names:lang})


print(dict)
