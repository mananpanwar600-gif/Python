# Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up! 

dict = {"Kese Ho": "How are you" , "Namaste": "Greetings" , "Chalo": "Lets go"}

word = input("Enter the word : ")
translation = dict.get(word)
if translation:
    print(f"The translation of word {word} is {translation}")
else:
    print("Word not found")