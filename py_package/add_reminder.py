import os
import datetime
import time
from threading import Timer

def validateTime(reminderTime):
    now = datetime.datetime.now()
    # print(now.hour, " ", now.minute)
    if(now.hour <= reminderTime.hour and now.minute <= reminderTime.minute):
        # print("Proper reminder time")
        return True
    else:
        print("Invalid reminder time")
        return False

def myJob():
    print("Hello world")
    pass

def addReminderToFile(userName, title, reminderTime):
    now = datetime.datetime.now()
    hour_diff = reminderTime.hour - now.hour
    minute_diff = reminderTime.minute - now.minute

    time_in_minute = hour_diff*60 + minute_diff

    # time.sleep(time_in_minute*60)
    t = Timer(time_in_minute*60, myJob)
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

        print(reminder_time)
    except Exception as e:
        print("Please enter proper time ", e)
