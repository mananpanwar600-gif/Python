# Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’. 

f = open("poems.txt","r")

content = f.read()
if "twinkle" in content:
    print("Found")
else:
    print("Not found")

f.close()