'''It is a beginner-friendly Python game which requires minimal Python skills to create. Having said that, if you a good practice of at least "if-else" conditionals, you'll be eligible for writing a basic Snake, Water & Gun game. It is not wrong to say this popular game another version Rock, Paper & Scissors.

Snake wins against water as it defeats the water, whereas water is effective against gun as water drowns the gun and hence wins. The snake loses against gun as the gun kills the snake. This is the basic understanding behind the game. This game is an amazing Python project will can be made much more complex using loops and random generator.  '''
import random

def function():
    pass

list =[1,2,3]
play = input("Press Y to play or Press N key to quit : ")
round = 1
c_count = 0
p_count = 0

while True:

    if(play=='Y' or play=='y'):
        while round<=10:
            computer_choice = random.choice(list)
            user_choice = int(input("Press 1 to choose snake / Press 2 to choose water / Press 3 to choose Gun : "))

            if(user_choice > 3 or user_choice<1):
                print("INVALID CHOICE!! ,Try Again...")

            if(computer_choice == user_choice):
                print("Game Draws")
                round +=1
            
            elif(computer_choice == 1 and user_choice == 2):
                print("Yes I won")
                c_count +=1
                round+=1

            elif(computer_choice == 1 and user_choice == 3):
                print("CONGO!! , You won")
                p_count +=1
                round +=1

            elif(computer_choice == 2 and user_choice == 1):
                print("CONGO!! , You won")
                p_count +=1
                round +=1

            elif(computer_choice == 2 and user_choice == 3):
                print("Yes I won")
                c_count +=1
                round +=1
                
            elif(computer_choice == 3 and user_choice == 1):
                print("Yes I won")
                c_count +=1
                round +=1

            elif(computer_choice == 3 and user_choice == 2):
                print("CONGO!! , You won")
                p_count +=1
                round +=1

    if(play=='N' or play=='n'):
        print("You quit!!")
        break


    print("\n\nMY SCORE : ",c_count)
    print("YOUR SCORE : ",p_count)
    if(c_count>p_count):
        print("I WON!! BETTER LUCK NEXT TIME")
    elif(c_count == p_count):
        print("DRAW")
    else:
        print("CONGRATULATIONS, YOU WON")
    
    break

    
            
                 

