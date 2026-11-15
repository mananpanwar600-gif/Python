# A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams

spam_keywords = ["Make a lot of money","Buy now","subscribe","click this"]
text = input("Enter the text paragragh : ").upper()

for i in range(4):
    spam_keywords[i] = spam_keywords[i].upper()

for keyword in spam_keywords:
    if keyword in text:
        isSpam = True
        break
    else:
        isSpam = False

if isSpam is True:
    print("SPAM COMMENT")
else:
    print("SAFE")