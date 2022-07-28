# importing datetime and time modules for obtaining current date and
# formatting the dates
import time
from datetime import date
import datetime

# function to display the menu


def main_menu(username):
    if username == 'admin':
        print(f'Welcome {username}\n\nSelect an option\n\n'
              'r - register\n'
              'a - add task\n'
              'va - view all tasks\n'
              'vm - view my task\n'
              'gr - generate reports\n'
              'ds - statistics\n'
              'e - exit\n')
    else:
        print(f'Welcome {username}\n\nSelect an option\n\n'
              'a - add task\n'
              'va - view all tasks\n'
              'vm - view my task\n'
              'e - exit\n')

   # user chooses a menu option
    selection = input('What do you wish to do?\n')

    # user can register new users
    if (selection) == "r":
        reg_user(username)

        job_protocal = input('\nis there anything else you would like to do\ntype yes or no\n')
        if job_protocal == ('yes' or 'Yes' or 'YES'):
            main_menu(username)
        else:
            print('goodbye')

    # adding a task to a user
    elif (selection) == "a":
        add_task(username)

        job_protocal = input('\nis there anything else you would like to do\ntype yes or no\n')
        if job_protocal == ('yes' or 'Yes' or 'YES'):
            main_menu(username)
        else:
            print('goodbye')

       # option for viewing all task
    elif (selection) == "va":
        view_all()

        job_protocal = input('\nis there anything else you would like to do\ntype yes or no\n')
        if job_protocal == ('yes' or 'Yes' or 'YES'):
            main_menu(username)
        else:
            print('goodbye')

       # option to view the currently logged on user's task
    elif (selection) == "vm":
        view_mine(username)

        job_protocal = input('\nis there anything else you would like to do\ntype yes or no\n')
        if job_protocal == ('yes' or 'Yes' or 'YES'):
            main_menu(username)
        else:
            print('goodbye')

       # option to view statistics
    elif (selection) == "ds" and username == "admin":
        display_stats(username)

        job_protocal = input('\nis there anything else you would like to do\ntype yes or no\n')
        if job_protocal == ('yes' or 'Yes' or 'YES'):
            main_menu(username)
        else:
            print('goodbye')

       # option to generate reports
    elif (selection) == 'gr' and username == "admin":
        generate_reports(username)

        job_protocal = input('\nis there anything else you would like to do\ntype yes or no\n')
        if job_protocal == ('yes' or 'Yes' or 'YES'):
            main_menu(username)
        else:
            print('goodbye')

       # option to exit
    elif(selection) == 'e':
        print("logging out")

       # if no valid selection was made
    else:
        print("invalid choice")
        main_menu(username)

# function to register users


def reg_user(username):
   # to prevent having spaces in the username
    username = username.strip()

    # setting aside variables to read the text file contents as a whole
    # and as lines respectively

    with open('user.txt', 'r', encoding='utf-8-sig')as registry:
        lines = registry.read()
        line = registry.readlines()

        # looping through the number of lines to obtain lists
        # containing separated credentials
        for i in range(len(line)):
            parts = (line[i]).strip().split(',')

            # first is the username credentials
            first = parts[0]

        # prevent duplication
        while True:
            username = input('enter a username: ')
            if username in lines:
                print('user already exists, try again')

            else:
                False

                password = input('enter a password: ')
                confirm_password = input('confirm password: ')

                break

        # writing to file only if password has been confirmed and
        # username is valid
        if (confirm_password == password and username not in lines):

            with open('user.txt', 'a', encoding='utf-8-sig')as registry:
                registry.write(f'\n{username}, {password}')
        else:
            print('kindly enter a valid set of credentials')

# function to add tasks


def add_task(username):

    # default for the completion status of a newly assigned task
    default = 'no'

    # displaying the usernames of the current users after seperating
    # the credentials by stripping and splitting
    with open('user.txt', 'r', encoding='utf-8-sig')as registry:
        line = registry.readlines()
        lines = registry.read()

        # loop section that handles the seperation of credentials
        for i in range(len(line)):
            parts = (line[i]).strip().split(',')
            first = parts[0]
            credentials.append(first)
            print(first)

        print('\nthese are the users you currently have')
        print('\n')

        username = input('To whom do you wish to add a new task to?\n')

        if username in credentials:
            task = input('What task is being added\n')
            description = input('briefly explain the task\n')
            date_today = time.strftime("%d %b %Y")
            print('specify your due dates')
            day = int(input ('enter the day in number format (02 or 30 or 31)'))
            month = input('enter the month in short hand letter form ( Feb or Mar or Dec )')
            year = int(input('enter the year in complete format ( 2022 or 2021 or 1996)'))
            due_date = (f'{day} {month} {year}')

            completion = default

            added_task = (f'Username:\t{username}\n'
                          f'Title:\t\t{task}\n'
                          f'Description:\t{description}\n'
                          f'Date Assigned:\t{date_today}\n'
                          f'Due Date:\t{due_date}\n'
                          f'Completion:\t{completion}\n')

            print(added_task)

            # writing new tasks to task.txt

            with open('tasks.txt', 'a', encoding='utf-8-sig')as taskfile:

                taskfile.write(
                    f'\n{username}, {task}, {description}, {date_today}, {due_date}, {completion}')

        # defense for when invalid credentials are entered
        else:
            print('no such user exists')

# function to view all the tasks


def view_all():
    with open('tasks.txt', 'r+', encoding='utf-8-sig')as neattasks:
        lines = neattasks.readlines()
        count = 1
        for i in range(len(lines)):
            parts = lines[i].strip().split(",")

            print(f'\t\t\nTASK {count}')

            for j in range(len(headers)):
                print(f'{headers[j]}\t {parts[j]}')

            count += 1
            print('\n\n')

# function to view only the tasks of the user currently logged on


def view_mine(username):

    with open('tasks.txt', 'r+', encoding='utf-8-sig')as mytasks:

        lines_vm = mytasks.readlines()
        count = 1

        for i in range(len(lines_vm)):
            parts = lines_vm[i].strip().split(",")

            # the unique identifier marks the actual number of the task
            # while the count shows a user their number of tasks
            if parts[0] == username:
                print(
                    f'\t\t\nTHIS IS YOUR TASK {count}.\n\nUNIQUE IDENTIFIER: #{i+1}\n')

                for j in range(len(headers)):

                    # sourcing the current login
                    print(f'{headers[j]}\t {parts[j]}')

            else:
                continue

            count += 1

        # editing and marking a task as complete or exiting to the menu
        select_task = int(input(
            '\nSelect a task by typing the task number or enter -1 to return to main menu.\n'))

        if select_task == (-1):
            main_menu(username)

        for k in range(len(lines_vm)):
            completion = lines_vm[k].strip().split(',')

            # reassigning a task only when the task has not been completed
            if select_task == k + 1:

                choice = input(
                    f'Do you wish to reassign this task?\n{lines_vm[k]}\n (type yes or no)\n')

                if choice == (
                    'yes' or 'Yes' or 'YES') and (
                    completion[5] == (
                        ' no' or ' No' or ' NO')):
                    with open('user.txt', 'r', encoding='utf-8-sig')as registry:

                        user_line = registry.readlines()
                        user_lines = registry.read()

                        # loop section that handles the seperation of
                        # credentials to display all available users

                        for l in range(len(user_line)):
                            parts = (user_line[l]).strip().split(',')
                            first = parts[0]
                            credentials.append(first)
                            print(first)

                        print('these are the users you currently have')
                        print('\n')

                        # changing the user and the due dates
                        reassign = input(
                            'to whom from among these do you want to reassign the task to?\n')

                        due_date_choice = input(
                            'Do you also want to change the due date\n(type yes or no)\n')

                        if due_date_choice == 'yes':
                            
                            print('specify your due dates')
                            day = int(input ('enter the day in number format (02 or 30 or 31)'))
                            month = input('enter the month in short hand letter form ( Feb or Mar or Dec )')
                            year = int(input('enter the year in complete format ( 2022 or 2021 or 1996)'))
                            new_due_date = (f'{day} {month} {year}')
                            completion[4] = new_due_date
                            lines_vm[k] = (
                                f'{reassign},{completion[1]},{completion[2]},{completion[3]}, {completion[4]},{completion[5]}\n')

                        else:
                            lines_vm[k] = (
                                f'{reassign},{completion[1]},{completion[2]},{completion[3]},{completion[4]},{completion[5]}\n')

                        # set of code that overwrites the whole text document
                        # only after reading it
                        mytasks.seek(0)
                        mytasks.writelines(lines_vm)
                        mytasks.truncate()

                # condition for when a task is completed but the user tries to
                # edit
                elif completion[5] != (' no' or ' No' or ' NO') and choice == ('yes' or 'Yes' or 'YES'):
                    print(
                        'this task has already been completed. You cannot reassign it to a new user.\n')

                # condtions for when the user wishes to mark the task as
                # complete
                elif choice == 'no' or 'No' or 'No':
                    mark = input(
                        'Have you completed this task? Enter Yes or No\n')

                    if mark == 'yes' or 'Yes' or 'YES':
                        completion[5] = ' Yes'
                        lines_vm[k] = (
                            f'{completion[0]},{completion[1]},{completion[2]},{completion[3]},{completion[4]},{completion[5]}\n')

                    else:
                        print('kindly complete your task first')

                    mytasks.seek(0)
                    mytasks.writelines(lines_vm)
                    mytasks.truncate()

# function to display statistics


def display_stats(username):

    print('you must generate reports to view the most recent statistics if any changes were made prior\n')

    with open('task_overview.txt', 'r', encoding='utf-8-sig')as taskstats:
        tasksfile = taskstats.readlines()
        for i in range(len(tasksfile)):
            print(f'{tasksfile[i].strip()}')
        print('\n')

    with open('user_overview.txt', 'r', encoding='utf-8-sig')as userstats:

        usersfile = userstats.readlines()
        for i in range(len(usersfile)):
            print(f'{usersfile[i].strip()}')
        print('\n')

# function to generate reports


def generate_reports(username):

    # writing and reading to the files created
    with open('task_overview.txt', 'w', encoding='utf-8-sig')as taskov:
        with open('tasks.txt', 'r', encoding='utf-8-sig')as taskfile:

            completed_tasks = 0
            incomplete_tasks = 0
            overdue = 0
            percentage_incomplete = 0
            percentage_overdue = 0

            lines = taskfile.readlines()
            number_of_tasks = len(lines)

            for i in range(number_of_tasks):
                parts = lines[i].strip().split(',')

                if parts[5].strip() == 'yes' or parts[5].strip() == 'Yes' or parts[5].strip() == 'YES':
                    completed_tasks += 1

                incomplete_tasks = (number_of_tasks - completed_tasks)

                # using datetime module to manipulate the dates in the text
                # files
                now = date.today()
                then = parts[4].strip()
                from datetime import datetime
                then = (datetime.strptime(then, '%d %b %Y')).date()

                # calculating the difference between a current date and a due
                # date
                duration_overall = (now - then)
                duration_days = (now - then).days

                # checking for incomplete and overdue tasks
                if (parts[5].strip() == 'no' or parts[5].strip() ==
                        'No' or parts[5].strip() == 'NO') and (duration_days > 0):
                    overdue += 1

                percentage_incomplete = round(
                    (incomplete_tasks / number_of_tasks) * 100, 2)
                percentage_overdue = round(
                    (overdue / number_of_tasks) * 100, 2)

            # writing to the task overview text file
            taskov.write(f'{task_overview_headers[0]}\t{number_of_tasks}\n')
            taskov.write(f'{task_overview_headers[1]}\t{completed_tasks}\n')
            taskov.write(f'{task_overview_headers[2]}\t{incomplete_tasks}\n')
            taskov.write(f'{task_overview_headers[3]}\t{overdue}\n')
            taskov.write(
                f'{task_overview_headers[4]}\t{percentage_incomplete}%\n')
            taskov.write(
                f'{task_overview_headers[5]}\t{percentage_overdue}%\n')

    # opening and writing and reading the user overview file
    with open('user_overview.txt', 'w', encoding='utf-8-sig')as userov:
        with open('user.txt', 'r', encoding='utf-8-sig')as userfile:
            lines = userfile.readlines()
            number_of_users = len(lines)

            # list to store the usernames to compare with those in the task
            # file
            user_name = []

            for i in range(number_of_users):
                user_parts = (lines[i].strip().split(','))
                user_name.append(user_parts[0])

                total_assigned = 0
                percentage_OT_assigned = 0
                user_tasks_completed = 0
                percentage_OT_completed = 0
                percentage_OT_incomplete = 0
                user_tasks_overdue = 0
                percentage_OT_overdue = 0

                # using the task file to gather date for various desired
                # calculations
                with open('tasks.txt', 'r', encoding='utf-8-sig')as taskfile:
                    task_lines = taskfile.readlines()
                    number_of_tasks = len(task_lines)

                    for j in range(number_of_tasks):
                        task_parts = task_lines[j].strip().split(',')
                        if user_name[i] == task_parts[0]:
                            total_assigned += 1

                            if task_parts[5].strip() == 'yes' or task_parts[5].strip(
                            ) == 'Yes' or task_parts[5].strip() == 'YES':
                                user_tasks_completed += 1
                                percentage_OT_completed = round(
                                    (user_tasks_completed / total_assigned) * 100, 2)
                            percentage_OT_incomplete = (
                                100 - percentage_OT_completed)

                            # manipulating dates to get the overdue time
                            now_user = date.today()
                            then_user = task_parts[4].strip()
                            from datetime import datetime
                            then_user = (
                                datetime.strptime(
                                    then_user, '%d %b %Y')).date()

                            duration_overall_user = (now_user - then_user)
                            duration_days_user = (now_user - then_user).days

                            if (task_parts[5].strip() == 'no' or task_parts[5].strip(
                            ) == 'No' or task_parts[5].strip() == 'NO') and (duration_days_user > 0):
                                user_tasks_overdue += 1
                                percentage_OT_overdue = round(
                                    (user_tasks_overdue / total_assigned) * 100, 2)

                        percentage_OT_assigned = (
                            round((total_assigned / number_of_tasks) * 100, 2))

                    # writing to user overview file
                    userov.write(
                        f'{user_stats_headers[0]} {user_name[i]}\n'
                        f'{user_stats_headers[1]} {total_assigned}\n'
                        f'{user_stats_headers[2]} {percentage_OT_assigned}\n'
                        f'{user_stats_headers[3]} {percentage_OT_completed}\n'
                        f'{user_stats_headers[4]} {percentage_OT_incomplete}\n'
                        f'{user_stats_headers[5]} {percentage_OT_overdue}\n\n')

        userov.write(f'\n{user_overview_headers[0]}\t{number_of_users}\n')
        userov.write(f'\n{user_overview_headers[1]} {number_of_tasks}\n')


# list that stors the parts of the text files as seperate words
parts = []

# list to store tasks from statistics
tasks = []

# list containing the headings  task details
headers = ['Username:  ',
           'Title:\t',
           'Description:',
           'Date Assigned:',
           'Due Date:',
           'Completion:']

# list containing the headings  task overview
task_overview_headers = ['Total number of tasks:',
                         'Total completed tasks:',
                         'Total incomplete tasks:',
                         'Overdue tasks:',
                         'Percentage of Incomplete tasks:',
                         'Percentage of Overdue tasks:']

# list containing the headings  user overview
user_overview_headers = ['Total number of users:',
                         'Total tasks generated and tracked:']

# list containing the headings  user stats
user_stats_headers = ['Username:',
                      'Tasks assigned:',
                      'Percentage of all tasks assigned:',
                      'Percentage of assigned completed:',
                      'Percentage pending:',
                      'Percentage overdue:']

# strings to store credentials
username = ''
password = ''
confirm_password = ''
selection = ''

# list to store credentials
credentials = []

# reading user.txt to obtain log in credentials
with open('user.txt', 'r', encoding='utf-8-sig')as login:

    # setting aside variables to read the text file contents as a whole
    x = login.read()

    # user inputs their credentials
    username = input('enter your username')
    password = input('enter your password')

    # confirming if the entered credentials are valid
    if username and password not in x:
        print('username or password is incorrect')

    # printing the menu if credentials are valid
    elif username and password in x:
        main_menu(username)
