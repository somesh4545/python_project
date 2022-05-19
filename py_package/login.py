import os
from py_package import login, signup, add_task, edit_task, view_task, delete_task, add_reminder

def login():
    print("***************************************")
    print("\nPlease enter the details to get logged in: ")
    loginUserName = input("Username: ")

    userFileName = loginUserName + ".txt"
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, '../UserCredentials/' + userFileName)
    if not os.path.exists(filepath):
        print("No such user is registered, please signup.")
        signup.signup()
    else:
        loginPassword = input("Password: ")
        f = open(filepath, 'r')
        fileData = f.readlines()
        modifiedFileData = []

        for data in fileData:
            modifiedFileData.append(data.replace("\n", ""))

        storedUserName = modifiedFileData[0]
        storedPassword = modifiedFileData[1]

        f.close()
        
        if(loginUserName == storedUserName and storedPassword == loginPassword):
            respo = 0
            print("\nYou can perform following tasks here: ")
            
            while respo != 6:
                print("\n**********************************************************************")
                print("Press 1: Add task \nPress 2: Edit task \nPress 3: View task \nPress 4: Delete task \nPress 5: Add reminder \nPress 6: Exit")

                respo = int(input("\nEnter your choice: "))
                if(respo == 1):
                    add_task.add_task(loginUserName)
                elif(respo == 2):   
                    edit_task.edit_task(loginUserName)
                elif(respo == 3):
                    view_task.view_task(loginUserName)
                elif(respo == 4):
                    delete_task.delete_task(loginUserName)
                elif(respo == 5):
                    add_reminder.add_reminder(loginUserName)
                elif(respo == 6):
                    print("Exit")   
        else:
            print("Wrong credentials, please try again")
            login()
