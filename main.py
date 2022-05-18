from py_package import login, signup

print("Welcome to your task manager")

print("\nPress 1: Login \nPress 2: SignUp")
num = int(input("Enter you choice: "))
if(num == 1):
    login.login()
elif(num == 2):
    signup.signup()
else:
    print("Please enter valid input.")


    

