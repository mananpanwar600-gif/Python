'''
 Append To a File
Write a Python program to append text in “sample1.txt” and write the string “Hello, PYnative!” into it
'''

with open("sample1.txt","a") as f:
    content = "\nHello, PYnative!"
    f.write(content)
    