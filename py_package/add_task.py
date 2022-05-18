import os
from py_package import view_task
from random import randint

def getNextId(path):
    return randint(100, 999)  

def add_task(userName):

    taskFileName = userName + ".txt"
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname,'../UserTasks/'+ taskFileName)
    print("Please enter the following details about your task: ")
    taskTitle = input("Enter the task  title: ")
    taskDeadline = input("Enter the deadline for the task: ")

    f = open(filepath, "a+")
    getNewId = getNextId(filepath)
    if(getNewId == 1):
        f.write("Task1 ID : "+ str(getNewId))
    else:
        f.write("\nTask" +str(getNewId) +" ID : "+ str(getNewId)) 
    f.write("\nTask" +str(getNewId) +" Title : " + taskTitle)
    f.write("\nTask" +str(getNewId) + " Deadline : " + taskDeadline)

    f.close()