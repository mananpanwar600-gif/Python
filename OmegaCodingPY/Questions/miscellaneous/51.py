''''
Write a program to count occurrences of all characters within a string
Given:

str1 = "Apple"
Expected Outcome:

{'A': 1, 'p': 2, 'l': 1, 'e': 1}
'''

str1 = "Apple"
dict = {}

for char in str1:
    p = str1.count(char)
    dict[char] = p

print(dict)