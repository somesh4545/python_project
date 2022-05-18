from xml.etree.ElementTree import TreeBuilder


import os

def delete_task(userName):
    deleteFilePath = userName.lower() + ".txt"
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname,'../UserTasks/'+deleteFilePath)
    # lines = f.readlines()

    deleteId = input("Enter the ID of the task you want to delete: ")

    curr_line = 0
    with open(filepath, "r+") as f:
        datas = f.readlines()
        for data in datas:
            if data.startswith("Task"+deleteId):
                datas.pop(curr_line)
                datas.pop(curr_line)
                datas.pop(curr_line)
                break
            curr_line+=1    
        with open(filepath, 'w') as overwrite_file:
                overwrite_file.write("")
        with open(filepath, 'a+') as append_file:
            for line in datas:
                append_file.write(line) 