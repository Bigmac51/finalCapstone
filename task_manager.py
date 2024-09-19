# Notes:
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the
# program will look in your root directory for the text files.

# =====importing libraries===========
import os
from datetime import datetime, date

# =====Global Variables===========
DATETIME_STRING_FORMAT = "%Y-%m-%d"
task_list = []
task_no_list = []
username_password = {}
curr_user = ""
user_data = []
user_overview_str_global = ""
task_overview_str_global = ""


# =====Functions===========
def reg_user():
    # my_name = ""

    # - Request input of a new username
    new_username = input("New Username: ")

    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password

        with open("user.txt", "w") as out_file:
            # user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

    # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")


def reg_userv2():
    new_username = ""

    # - Request input of a unique new username or return to main menu
    unique_username = False
    while not unique_username:
        new_username = input("-1: Return to main menu or \nNew Username: ")
        if new_username in username_password.keys():
            print("Username already exists. Please add an alternative unique user name")
        elif new_username == "-1":
            # unique_username = True

            break

        else:
            print(new_username)
            unique_username = True

    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password
        print(username_password[new_username])

        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

    # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")


def add_task():
    """Allow a user to add a new task to task.txt file
        Prompt a user for the following:
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and
             - the due date of the task."""
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # - Get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")


def view_all():
    '''Reads the task from task.txt file and prints to the console in the
          format of Output 2 presented in the task pdf (i.e. includes spacing
          and labelling)
       '''

    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


def view_my_tasks():
    """Reads the task from task.txt file and prints to the console in the
   format of Output 2 presented in the task pdf (i.e. includes spacing
   and labelling)
    """
    for t in task_list:
        if t['username'] == curr_user:
            # Displays the task with a corresponding number
            print("\nTask No: \t\t" + str(list(task_list).index(t) + 1))
            task_no_list.append(list(task_list).index(t) + 1)

            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \t {t['description']}\n"
            disp_str += f"Task Completed: \t {t['completed']}"
            print(disp_str)

    user_task_input = ""
    task_edit_no = 0
    user_task_check = False
    while not user_task_check:
        # Allows user to select a specific task by corresponding number to mark as complete or edit
        task_edit_no = int(input("\nPlease select a task to edit using the task number above or "
                                 "-1: Return to the main menu."
                                 "\nEnter task number to edit task or mark task as complete"
                                 "\n: "))

        if task_edit_no == -1:
            user_task_check = True
            break
        elif not task_edit_no in task_no_list:
            print("Incorrect task number entered, please try again.")
        else:
            user_task_input = input("\nPlease select from the following options below:"
                                    "\nj: Mark Task for Completion"
                                    "\nk: Edit the task"
                                    "\n-1: Return to main menu"
                                    "\n: ").lower()

        if user_task_input == "j":
            if task_list[task_edit_no - 1]["completed"]:
                print("Task already marked as complete \n")
                user_task_check = True
            else:
                # - Marks the task as complete
                print("---------- Marks the task as complete ---------- \n")
                print(task_list)

                task_list[task_edit_no - 1]["completed"] = True
                print("Task marked as Complete \n")
                print(task_list)

                with open("tasks.txt", "w") as task_file:
                    task_list_to_write = []
                    i = 0
                    while i < len(task_list):
                        str_attrs = [
                            task_list[i]["username"],
                            task_list[i]["title"],
                            task_list[i]["description"],
                            task_list[i]["due_date"].strftime("%Y-%m-%d"),
                            task_list[i]["assigned_date"].strftime("%Y-%m-%d"),
                            "Yes" if task_list[i]["completed"] else "No"
                        ]
                        print(str_attrs)

                        i += 1
                        task_list_to_write.append(";".join(str_attrs))
                    task_file.write("\n".join(task_list_to_write))
                print("Task file successfully updated.")

                user_task_check = True

        if user_task_input == "k":
            if task_list[task_edit_no - 1]["completed"]:
                print("Task already marked as complete \n")
                user_task_check = True
                break
            else:
                # - Edit the task if it is not completed
                print("---------- Edit the task ---------- \n")

                print("Task No: \t" + str(list(task_list).index(t) + 1))
                print("Task: \t" + task_list[task_edit_no - 1]["title"])
                print("Assigned to: \t" + task_list[task_edit_no - 1]["username"])
                print(
                    "Date Assigned: \t" + task_list[task_edit_no - 1]['assigned_date'].strftime(DATETIME_STRING_FORMAT))
                print("Due Date: \t" + task_list[task_edit_no - 1]['due_date'].strftime(DATETIME_STRING_FORMAT))
                print("Task Description: \t" + task_list[task_edit_no - 1]["description"])
                print("Task Completed: \t" + str(task_list[task_edit_no - 1]["completed"]))

            user_task_input = input("\nPlease select from the following options below:"
                                    "\nx: Change username of the task"
                                    "\ny: Change the due date of the task"
                                    "\n-1: Return to main menu"
                                    "\n: ").lower()
            #

            if user_task_input == "x":
                with open("user.txt", 'r') as user_file:
                    user_data = user_file.read().split("\n")

                    username_password = {}
                    for user in user_data:
                        username, password = user.split(';')
                        username_password[username] = password

                    print(username_password)

                    user_str = ""
                    for user in username_password:

                        if user == curr_user:
                            continue
                        user_str += str(list(username_password).index(user)) + ": " + "\t" + user + "\n"

                    username_task_change = input("\nPlease select new username using coresponding number, "
                                                 "from the list below to assign to task:"
                                                 + "\n" + user_str + ": ")

                    print(task_list)
                    print(task_list[task_edit_no - 1]['username'])
                    print(task_list[task_edit_no - 1]['title'])
                    print(task_list[int(username_task_change)]['username'])

                    task_list[task_edit_no - 1]["username"] = task_list[int(username_task_change)]['username']

                    print(task_list)

                with open("tasks.txt", "w") as task_file:
                    task_list_to_write = []
                    i = 0
                    while i < len(task_list):
                        str_attrs = [
                            task_list[i]["username"],
                            task_list[i]["title"],
                            task_list[i]["description"],
                            task_list[i]["due_date"].strftime("%Y-%m-%d"),
                            task_list[i]["assigned_date"].strftime("%Y-%m-%d"),
                            "Yes" if task_list[i]["completed"] else "No"
                        ]
                        print(str_attrs)

                        i += 1
                        task_list_to_write.append(";".join(str_attrs))
                    task_file.write("\n".join(task_list_to_write))
                print("\n Task file successfully updated. \n \n")

                user_task_check = True

                print("\n")

            if user_task_input == "y":
                print(task_list)
                print(task_list[task_edit_no - 1]['due_date'])
                print(task_list[task_edit_no - 1]['title'])

                task_due_date1 = input("Enter new due date of task in format(YYYY-MM-DD): ")
                due_date_time1 = datetime.strptime(task_due_date1, DATETIME_STRING_FORMAT)

                print(due_date_time1)

                task_list[task_edit_no - 1]['due_date'] = due_date_time1

                print(task_list)

                print("\n")

                with open("tasks.txt", "w") as task_file:
                    task_list_to_write = []
                    i = 0
                    while i < len(task_list):
                        str_attrs = [
                            task_list[i]["username"],
                            task_list[i]["title"],
                            task_list[i]["description"],
                            task_list[i]["due_date"].strftime("%Y-%m-%d"),
                            task_list[i]["assigned_date"].strftime("%Y-%m-%d"),
                            "Yes" if task_list[i]["completed"] else "No"
                        ]
                        print(str_attrs)

                        i += 1
                        task_list_to_write.append(";".join(str_attrs))
                    task_file.write("\n".join(task_list_to_write))
                print("\n Task file successfully updated. \n \n")

                user_task_check = True

            if user_task_input == "-1":
                print("hi")
                user_task_check = True

        if user_task_input == "-1":
            print("hi2")

            user_task_check = True


def generate_reports():
    print("reports generating...")

    user_overview_str = ""

    i = 0
    tasks_completed = 0
    tasks_uncompleted_overdue = 0
    tasks_overdue = 0

    totalno_tasks = int(len(task_list))
    while i < len(task_list):

        if task_list[i]["completed"]:
            tasks_completed += 1

        due_date = task_list[i]["due_date"]
        asigned_date = task_list[i]["assigned_date"]
        today_date = datetime.now()

        remaining_date = due_date - today_date
        remaining_date_days = int(remaining_date.days)

        if remaining_date_days < 0 and not task_list[i]["completed"]:
            tasks_uncompleted_overdue += 1

        if remaining_date_days < 0:
            tasks_overdue += 1

        i += 1

    task_overview_str = f"Total number of tasks: \t {len(task_list)}\n"

    task_overview_str += f"Total number of completed tasks: \t {tasks_completed}\n"

    task_overview_str += f"Total number of uncompleted tasks: \t {totalno_tasks - tasks_completed}\n"

    task_overview_str += f"Total number of uncompleted tasks, that are also overdue: \t {tasks_uncompleted_overdue}\n"

    task_overview_str += f"Percentage of tasks that are incomplete: \t {((totalno_tasks - tasks_completed) / totalno_tasks) * 100} % \n"

    task_overview_str += f"Percentage of tasks that are overdue: \t {(tasks_overdue / totalno_tasks) * 100} % \n"

    task_overview_str += "----------------------------------- \n \n"

    # - Write to task_overview.txt file
    with open("task_overview.txt", "w") as task_file:

        task_file.write(task_overview_str)

    print("Task Overview file generated successfully.\n \n")

    # - task_overview.txt END

    # - user_overview.txt START

    user_overview_str += f"Total number of users registered: \t {len(user_data)}\n"
    user_overview_str += f"Total number of tasks generated: \t {len(task_list)}\n \n"

    username_list = []
    user_notasks_assigned = []

    usertasks_assigned = 0
    usertasks_assignedrecorded = 0
    usertasks_completed = 0
    usertasks_uncompleted_overdue = 0
    usertasks_overdue = 0
    usertasks_percentageasigned = 0

    for user in username_password:
        username_list.append(user)

        m = 0
        while m < len(task_list):
            if task_list[m]["username"] == user:
                usertasks_assigned += 1

            due_date = task_list[m]["due_date"]
            today_date = datetime.now()
            remaining_date = due_date - today_date
            remaining_date_days = int(remaining_date.days)

            if task_list[m]["username"] == user and remaining_date_days < 0 and not task_list[m]["completed"]:
                usertasks_uncompleted_overdue += 1

            m += 1

        user_overview_str += f"Total number of tasks assigned to user {user}: \t {usertasks_assigned}\n"

        user_notasks_assigned.append(usertasks_assigned)
        usertasks_assignedrecorded = usertasks_assigned
        usertasks_assigned = 0
        user_indexvalue = username_list.index(user)
        usertasks_percentageasigned = round((user_notasks_assigned[user_indexvalue] / len(task_list)) * 100)

        user_overview_str += f"Percentage of total number of tasks assigned to user {user}: \t {usertasks_percentageasigned}%\n"

        g = 0
        while g < len(task_list):
            if task_list[g]["username"] == user and task_list[g]["completed"]:
                usertasks_completed += 1

            g += 1

        user_overview_str += f"Percentage of the tasks assigned to user {user}, that have been completed: \t {round((usertasks_completed / usertasks_assignedrecorded) * 100)}%\n"
        user_overview_str += f"Percentage of the tasks assigned to user {user}, that must still be completed: \t {100 - round((usertasks_completed / usertasks_assignedrecorded) * 100)}%\n"
        user_overview_str += f"Percentage of the tasks assigned to user {user}, that must still be completed and are overdue: \t {round((usertasks_uncompleted_overdue / usertasks_assignedrecorded) * 100)}%\n \n"
        user_overview_str += "----------------------------------- \n \n"

        usertasks_uncompleted_overdue = 0
        usertasks_completed = 0

    # - rite to user_overview.txt file
    with open("user_overview.txt", "w") as task_file:

        task_file.write(user_overview_str)

    print("User Overview file generated successfully.\n \n")

    # - user_overview.txt END


def display_statistics():
    generate_reports()

    '''If the user is an admin they can display statistics about number of users
            and tasks.'''
    num_users = len(username_password.keys())
    num_tasks = len(task_list)

    print("-----------------------------------")
    print(f"Number of users: \t\t {num_users}")
    print(f"Number of tasks: \t\t {num_tasks}")
    print("-----------------------------------")
    print(" \n")

    # - Read in task_overview_data and display content to screen
    f = open('task_overview.txt', 'r')
    task_overview_data = f.read()
    f.close()
    print(task_overview_data)

    # - Read in user_overview_data and display content to screen
    f = open('user_overview.txt', 'r')
    user_overview_data = f.read()
    f.close()
    print(user_overview_data)

    print(" \n")


# ============================
# =====Main Program===========
# ============================


# - Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []
for t_str in task_data:
    curr_t = {}

    # - Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)

# ====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# - If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# - Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# - Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

    print(username_password)

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

while True:
    # - Presenting the menu to the user and making sure that the user input is converted to lower case.

    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        '''Add a new user to the user.txt file'''
        reg_userv2()

    elif menu == 'a':
        '''Allow a user to add a new task to task.txt file'''
        add_task()

    elif menu == 'va':
        '''Allow a user to view all the tasks listed in task.txt file'''
        view_all()

    elif menu == 'vm':
        '''Allow a user to view all the tasks that have been assigned to them in the task.txt file'''
        view_my_tasks()

    elif menu == 'gr':
        '''Allow a user to generate reports in the .txt file'''
        generate_reports()

    elif menu == 'ds' and curr_user == 'admin':
        display_statistics()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
