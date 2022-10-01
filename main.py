import string
import random

def Main():
    #Asks how many characters of password the user wants and saves it into "CharNum"
    CharNum=int(input("How many characters do you want ? "))


    #Generating a string with 0-9 , a - z , A - Z and adding it to "Test" varible
    Test=string.digits+string.ascii_lowercase+string.ascii_uppercase+string.punctuation

    #Picking random string from the string varible "Test" , "CharNum" defines how many characters there should be in the password
    Password=''.join(random.choice(Test) for i in range(CharNum)) 
   
    print(Password)
    
    with open("saved.txt", mode ="a") as passfile:
        passfile.write(Password+"\n")
        
    print("Password has been stored in saved.txt") 
    Main()
    
Main()
