import os

def update_file(file_path, id, new_title, new_deadline):
    pass
    with open(file_path, 'r') as f:
        data = f.readlines()
        cur_line_no, found_line_no = 0, 0
        for line in data:
            cur_line_no += 1
            if(line.startswith(id)):
                found_line_no = cur_line_no
                break
        
        if(found_line_no == 0):
            print("ID does not exist")
        else:
            # file_content = data
            data.pop(found_line_no)
            data.pop(found_line_no)
            data.insert(found_line_no, id+" Title: "+new_title+"\n")
            data.insert(found_line_no+1, id+" Deadline: "+new_deadline+"\n")
            with open(file_path, 'w') as overwrite_file:
                overwrite_file.write("")
            with open(file_path, 'a+') as append_file:
                for line in data:
                    append_file.write(line) 

def edit_task(userName):
    id = input("Enter task id: ")
    id = "Task"+id

    new_title = input("Enter task new title: ")
    new_deadline = input("Enter task deadline: ")

    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, '../UserTasks/' + userName.lower()+".txt")

    update_file(filepath, id, new_title, new_deadline)
    return