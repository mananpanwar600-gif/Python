'''
 Read a File
Write a Python program to read the entire contents of a text file named “sample.txt” and print it to the console.
'''

file = open("sample.txt","r")

content = file.read()
print(content)
file.close()