# Write a python function to remove a given word from a list ad strip it at the same 
# time. 

def remove(list,word):
        res = word.strip()
        if(res in list):
            list.remove(res)
        print(list)
        print(res)

list = ["Hello","World","Code","Python","programming"]  
word = input("Enter the number to be removed : ")

remove(list,word)