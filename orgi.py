
#!./bin/python

import time;
import datetime;
import calendar;

from OrgiTask import OrgiTask

intro = ''' 
This is an organizer program. I start it up and it randomly assigns a project for the day. It mixes together 1 important task and 1 project task.
It also stores and checks off these projects in time.

The program will store this information into a file.
These files can be edited through the program or manually.
Before the files are overwritten they will be backed up.


'''

# print(intro)

message = '''
Hi Grisha today is: %s
Your global task list includes the following items:
'''




# First I will need to use a calender program

# This program could be a couple things.
# First it could be a command line program which takes user input and
# displays some corresponding info
# Second it could be a command line tool that will spit out what you want
# from command line arguments
# Thirdly it could have a GUI through which I could actually update stuff
# I think first thing is to create a generic structure for the application
# and then use that structure through different interfaces
# ideally this thing could kind of run my life. I would put in these tasks
# and ideas and it would decide what I focus on for a given day
# it could even be like an operating system task scheduler with a priority
# system

if __name__ == '__main__':
    # TODO: Query user for Tasks and display them


    localtime = time.localtime(time.time())
    asciitime = time.asctime(localtime)
    now_cal = calendar.month(localtime.tm_year, localtime.tm_mon)
    print (now_cal)    
    print("%s\n" % asciitime)

    
    user_input_task = input("Enter a new task for today: ")
    new_task = OrgiTask(user_input_task)
    # Task creation info
    t_cr = new_task.created
    # Open a file and write the new task to it
    tasks_file = open("Tasks.txt", "a")
    #  Write task to file
    task_lines = [
        f"Task: {new_task.description}\n",
        f"date created: {t_cr.tm_mon}/{t_cr.tm_mday}/{t_cr.tm_year}\n",
        f"time created: {t_cr.tm_hour}:{t_cr.tm_min}:{t_cr.tm_sec}\n"
        f"timezone: {new_task.created_tz}\n"
    ]
    tasks_file.writelines(task_lines)
    tasks_file.close()
    
    

    

