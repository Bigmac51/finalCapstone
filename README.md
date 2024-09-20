○ Project name: 
Final Capstone Project


○ Table of Contents
   Project Description
   Installation Procedure
   Usage Instructions
   Creditd
   


○ Project Description:
The task was to modify the existing task_manager.py code to extend its functionality.
The additional functionality required varied from registering a user, adding a task, 
viewing all tasks, and viewing the current user's tasks. Using the principle of 
abstraction, refactoring, the code can be made into a more managable streamlined codebase. 



○ Installation Procedure
The Python file is downloadable, an can be inserted into a project folder once setup has taken place using the below instructions.

 Here’s a step-by-step guide to installing and running a Python file in an IDE, using PyCharm as an example:
1. Install Python
Download Python: Go to the official Python website and download the latest version for your operating system.
Run the Installer: Execute the downloaded file and follow the installation instructions. Make sure to check the option to add Python to your PATH.
2. Install PyCharm
Download PyCharm: Visit the JetBrains website and download the Community Edition of PyCharm.
Run the Installer: Execute the downloaded file and follow the setup wizard. Choose your installation options, such as creating a desktop shortcut and associating .py files with PyCharm.
Launch PyCharm: After installation, open PyCharm.
3. Create a New Project
Start a New Project: On the Welcome screen, click “New Project”.
Configure the Project: Choose a location for your project and ensure the correct Python interpreter is selected. PyCharm should automatically detect the Python installation.
4. Run Your Python File
Locate Your File: In the Project tool window, find your Python file.
Run the File: Right-click on the file and select “Run ‘<filename>’”. You should see the output in the Run tool window at the bottom




○ Usage Instructions
The code is a task management system written in Python. The user is presented with a series of prompts which vary depending upon the option choosen. This system allows users to register, log in, manage tasks, and generate reports. 
It utilizes a simple text file storage mechanism to keep track of users and tasks.

The code contains several functions that encapsulate various functionalities:

User Registration (`reg_user`, `reg_userv2`)**:
  - These functions allow new users to register by entering a username and password. They check for unique usernames and ensure passwords match before storing them in a text file.

Adding Tasks (`add_task`)**:
  - This function enables users to create new tasks. It collects details such as the task's title, description, due date, and the username of the person assigned to the task.
  - It also checks if the assigned username exists before adding the task to a list and saving it to a file.

Viewing Tasks (`view_all`, `view_my_tasks`)**:
  - `view_all` displays tasks for all users, while `view_my_tasks` filters tasks to show only those assigned to the currently logged-in user. They format the output with labels for better readability.

Generating Reports (`generate_reports`, `display_statistics`)**:
  - These functions allow the admin user to generate and display reports, providing insights into task completion statistics and user activity.



○ Credits
M. Campbell


