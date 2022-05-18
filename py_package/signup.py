import os
from py_package import login

def signup():
    print("***************************************")
    print("\nProvide the following details: ")
    userName = input("\nEnter your username: ")
    
    userFileName = userName + ".txt"
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname,'../UserCredentials/', userFileName)
    if os.path.exists(filepath):
        print("This username is already taken, please try again.")
        signup()
    else:
        passWord = input("Enter your password: ")
        f = open(filepath, "a")
        f.write(userName)
        f.write("\n" + passWord)
        f.close()
        login.login()