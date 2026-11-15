#  Write a program to find out whether a given post is talking about “Harry” or not. 

post = input("Enter the post : ")
updated_post = post.lower()

if "harry" in updated_post:
    print("YES!")
else:
    print("No")