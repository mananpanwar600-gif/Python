'''
 Read Specific Lines From a File
Write a Python program to read only the first 5 lines of “sample.txt”.

'''

try:
    with open("sample.txt","r") as f:
        for i in range(5):
            print(f.readline().strip())

except Exception as e:
    print(e)