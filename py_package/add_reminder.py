import os
import datetime
import time
from threading import Timer
from plyer import notification

reminder_title = []

def validateTime(reminderTime):
    now = datetime.datetime.now()
    if(now.hour <= reminderTime.hour and now.minute <= reminderTime.minute):
        # print("Proper reminder time")
        return True
    else:
        print("Invalid reminder time")
        return False

def sendNotification():
    title = reminder_title[0]
    reminder_title.pop(0)
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, '../assets/logo.ico')
    notification.notify(
            title = title,
            message="This is a notification message from task manager" ,
            app_name="Task Manager",
            app_icon = filepath
    )
    pass

def addReminderToFile(userName, title, reminderTime):
    now = datetime.datetime.now()
    hour_diff = reminderTime.hour - now.hour
    minute_diff = reminderTime.minute - now.minute

    time_in_minute = hour_diff*60 + minute_diff

    # time.sleep(time_in_minute*60)
    reminder_title.append(title)
    t = Timer(time_in_minute*60, sendNotification)
    t.start()
    # print("Reminder time")
    pass

def add_reminder(userName):
    # print("\a")
    reminder_name = input("Enter reminder title: ")
    reminder_time = input("Enter reminder time in HH:MM format: ")
    
    try: 
        # h, m = map(int, remainder_name.split(":"))
        reminder_time = datetime.datetime.strptime(reminder_time, "%H:%M")

        if(validateTime(reminder_time) == True):
            addReminderToFile(userName, reminder_name, reminder_time)
        else:
            pass

    except Exception as e:
        print("Please enter proper time ", e)
