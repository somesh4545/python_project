import os

def view_task(userName):
    viewFilePath = userName + ".txt"
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, '../UserTasks/'+viewFilePath)
    f = open(filepath, "r+")
    # lines = f.readlines()
    print(f.read())