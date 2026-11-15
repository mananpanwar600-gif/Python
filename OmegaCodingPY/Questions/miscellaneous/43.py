''''
Check Whether a password is strong or not
'''
def check_password(password):
        if(len(password)>8):
            if(password.isnumeric()):
                print("WEAK PASSWORD!! Use special character,numbers and alphabets")
                  
            elif(password.isalpha()):
                print("WEAK PASSWORD!! Use special character,numbers and alphabets")
                
            elif(password.isalnum()):
                print("Good!! But could be more strong...")
             
            else:
                 print("STRONG PASSWORD!!")
        else: 
            print("Password must contain more than 8 characters")
          
             
p = input("Enter the password : ")

check_password(p)
