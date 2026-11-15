'''
Count Unique Words
Write a code to count the number of unique words in the given a sentence.

Given:

sentence = "dog is a simple animal dogs is selfless animal"
Expected Output:


Number of unique words: 7
'''

sentence = "dog is a simple animal dogs is selfless animal"
s = set(sentence.split())

count = 0

while count<len(s):
    count += 1

print("Number of unique words :",count)