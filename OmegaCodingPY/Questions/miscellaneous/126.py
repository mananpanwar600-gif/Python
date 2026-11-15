'''
 Write To a File
Write a Python program to create a new file named “sample1.txt” and write into it.
'''

with open("sample1.txt","w") as f:
    content = """Matarose never comes home
She's hungry like a wolf
She's rosa de mota in lacroix"""
    
    f.write(content)