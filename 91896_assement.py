from easygui import *


tasks = {
    "T1":{
        "Title":"Design Homepage",
        "Description":"Create a mockup of the homepage",
        "Assignee":"JSM",
        "Priority":3,
        "Status":"In Progress"

    },
    "T2":{
        "Title":"Implement Login page",
        "Description":"Create the Login page for the website",
        "Assignee":"JSM",
        "Priority":3,
        "Status":"Blocked"

    },
    "T3":{
        "Title":"Fix navigation menu",
        "Description":"Fix the navigation menu to be more user-friendly",
        "Assignee":"None",
        "Priority":1,
        "Status":"Not Started"

    },
    "T4":{
        "Title":"Add payment processing",
        "Description":"Implement payment processing for the website",
        "Assignee":"JLO",
        "Priority":2,
        "Status":"In Progress"

    },
    "T5":{
        "Title":"Create an About Us page",
        "Description":"Create a page with information about the company",
        "Assignee":"BDI",
        "Priority":1,
        "Status":"Blocked"

    },
}

team_members = {
    "JSM":{
        "Name":"John Smith",
        "Email":"John@techvision.com",
        "Tasks Assigned":["T1","T2"],
    },
    "JLO":{
        "Name":"Jane Love",
        "Email":"Jane@techvision.com",
        "Tasks Assigned":["T4"],
    },
    "BDI":{
        "Name":"Bob Dillon",
        "Email":"Bob@techvision.com",
        "Tasks Assigned":["T5"],
    },

}

#Constant variables
#A list of all the inputs/details of a task.
Input_list = ["Title","Description","Assignee","Priority","Status"]

#A list of all the possible status for a task.
Status_list = ["Not Started","In Progress","Blocked","Completed"]

#A list of all inputs/details of a team member.
Member_details = ["Name","Email","Tasks Assigned"]

def display(type,specific):
    ''' This function is used to display a task or team members full 
    descrition/details. The Function takes in a type parameter which 
    tells the function wheter it needs to display a Task or
    team member and the specific parameter tells the function what task
    or team memeber specfically to display. The function then creates a
    string variable with the details of the specfic task/team member and
    returns it. 
    
    Keyword arguments:
    type -- the dict in which the specfic item details are
    specfic -- the specfic item in the dict of type
    '''
    #An empty string to which the message will be added to and then
    #returned to where this function is called. 
    message = ''
    message += (f"\n{specific} :")

    #An if statement which appends to the message depending on if it is
    #in the tasks dictionary or the team member dictionary.
    if type == "Task":
        # A formated string that will formats all the details of the 
        #specific task put in the parameter of the function.
        for input in Input_list:
            message += (f"\n   {input}: {tasks[specific][input]}")

    elif type == "Team member":
        # A formated string that will formats all the details of the 
        #specific team member put in the parameter of the function.
        for details in Member_details:
            message += (f"\n     {details}: {team_members[specific][details]}")

    return message


def assignee_task_removal(attribute,value,task):
    '''
    This function is run when the program has a task has a completed 
    status to then remove that task from the assignee's task list.

    keyword arguments:
    attribute -- the detail of the task at that when the function is
    called.
    value -- The value of the attribute.
    task -- The key of the task.
    '''

    #An if statement that checks if the attribute parameter inputed is
    #status and if it's value is equal to 'Completed'. 
    if attribute == 'Status' and value == 'Completed':
        #An variable that holds teh Assignee of the task inputed in the
        #task parameter when the function is called.
        assignee = tasks[task]['Assignee']  

        #An if statement that checks if the assignee variable does
        #not equal "None"
        if assignee != "None":
            #This removes the task from the assignee's tasks assigned
            #list.
            team_members[assignee]["Tasks Assigned"].remove(task)


def new_task():
    ''' This function is run when the user wants to add a new task to 
    the tasks dictionary. It runs through all inputs in a for loop then 
    checks if any input is empty and ask for it again until all value 
    are not empty. ''' 
    
    #An empty list that all the new task's details get appended to.
    output = []
    # task_num is a variable that determine the key for the new function
    #based on he amount of tasks that already exists and adds a number 
    #to that which then gets appened to the output list.
    task_number = len(list(tasks.keys())) + 1
    output.append(f"T{task_number}")

    #A for loop that runs through all the inputs/details that are needed
    #for the the new task being made and then appends it to the output 
    #list.
    for attribute in Input_list:
        detail = value_change(attribute)
        
        #An if statement that checks if the detail variable equals none
        #and if it does then returns None.
        if not detail:
            return 
        #Appends the detail to the variable named output which is a 
        #list.
        output.append(detail)
        #Runs the assignee_task_removal function to see if the task's
        #status is completed and if so then remove it from the 
        #assignee's task assigned list.
        assignee_task_removal(attribute,detail,output[0])

    #Updates the tasks dictionary witht the new task using the output 
    #list which has all the details of the new task.
    tasks.update({output[0]:{
        "Title":output[1],
        "Description":output[2],
        "Assignee":output[3],
        "Priority":output[4],
        "Status":output[5]

    }})

    return 


def update_task():
    '''This function is run when the user wants to update a 
    pre-existing task. It asks the user first what task then what
    specfic detail they want to change of that the task then asks for 
    the value and then updates that specfic value to the specfic task
    they choose.
    '''
    #The task the user has picked, this is determined by using the
    #search function.
    chosen_task = search("Task")

    #An if statement that checks if the chosen_task variable equals None
    #and if it does then returns None.
    if not chosen_task:
        return 
    
    #The detail/attribute the user wants to change of their choosen 
    #task.
    attribute = buttonbox("What do you want to change?", choices = Input_list)
    #An if statement that checks if the detail variable equals None
    #and if it does then returns None meaning it will go back to the 
    #menu and not update the attribute's value.
    if not attribute:
        return 
        
    #Using the value change function the ask the user what them the new
    #value for the detail they want to change.
    changed_value = value_change(attribute)
    
    #An if statement that checks if the changed_value variable equals 
    #None and if it does then returns None meaning it will go back to 
    #the menu and not update the attribute's value.
    if not changed_value:
        return 
    
    #This updates the chosen detail in the chosen task.
    tasks[chosen_task[0]][attribute] = changed_value

    #An if statement that checks if the user has changed the status of 
    #their choosen task and if that choosen task is completed. This to 
    #see if the task needs to be removed from the assignees task list.
    assignee_task_removal(attribute,changed_value,chosen_task[0])
   
    return 


def value_change(attribute):
    '''A function that is used to determine any detail/attribute of a 
    task, that could be determining new details for a new task or 
    figuring out what is the new value for a detail being updated.

    keyword arguments:
    attribute -- the detail being asked to the user for a value
    '''
    #Makes a list of all possible assigness or the keys of the team
    #member list.
    assignee_list = list(team_members.keys())
    assignee_list.append("None")
    value = ''

    #A while loop that runs while the value string is empty.
    while value == '': 
        #An series of if and elif statements that checks what the 
        #attribute is then asks then uses the approriate easygui box to 
        #ask the user the value of the attribute inputed into the 
        #function.
        if attribute == "Title" or attribute == "Description":
            #To determine the value an enterbox is called when the 
            #attribute is "Title" or "Description" as both reponses 
            #can have a range of possible values. 
            value = enterbox(f"what is the {attribute}?")

        elif attribute == "Assignee":
            #Determining what the value is by using a buttonbox to asks 
            #the user who the asignee is.
            value = buttonbox(f"Who is the assignee?","Assignee",assignee_list)

        elif attribute == "Priority":
            #Determinging what the value is when the detail is priority
            #by using a integerbox and having a upper and lowerbound 
            #from 1-3.
            value = integerbox(f"What is the priority?","Priority", \
                               lowerbound=1, upperbound=3)
            
        elif attribute == "Status":
            #Determening what the value is when the detail is status by
            #using a buttonbox and having buttons of a list of all the 
            #possible statuss a task can have.
            value = buttonbox(f"what is the status?","Assignee",Status_list)

        #An if statement that checks if the value is an empty string.
        #This is just to tell the user that they need to input a value.
        if value == '':
            #A message box to tell the user that they haven't input 
            #anything
            msgbox("Value needs to be inputed")
        
        #An elif statement that checks of value or attribute equal None
        #then returns None to stop the function and stoping it from
        #returning the value variable.
        elif not value or not attribute:
            return 
   
    return value


def search(type):
    '''This task take a type parameter , task or team member, then makes
    a list of all the keys of that type then runs a for loop to figure 
    out the the title of the task or the name of the team member then
    outputs a choicebox according the the avaible choices of the type 
    the user chooses in title or name form instead of keys. Then in the
    end returns the key in which the choosen title/name is , 
    then what the choice is title/name form and also a list of all the 
    choices the user had to choose from.
    
    keyword arguments :
    type -- The dictionary which will be searched in
    '''

    #An empty list variable that will get appended to save the users
    #possible choices depending on what the type parameter is when the
    #the function is called.
    choices = []
    
    #An if/elif statement that checks whether the type is 'Task'.
    if type == "Task":
        #A variable that saves a list of all the keys of the task list.
        keys = list(tasks.keys())

        #A for loop that runs through all the keys in the tasks 
        #dictionary and appends a f string with the key then it's 
        # 'Title' attribute to the choices list.
        for key in tasks:
            choices.append(f"{key} - {tasks[key]['Title']}")

    #An elif statement that checks whether the type is 'Team member'.
    elif type == "Team member":
        #A variable that saves a list of all the keys of the 
        #team_members list.
        keys = list(team_members.keys())

        #A for loop that runs through all the keys in the team_member 
        #dictionary and appends a f string with the key then it's 
        #'Name' attribute to the choices list.
        for name_code in team_members:
            choices.append(f"{team_members[name_code]['Name']}")
    
    #A variable that saves the users choice from a choicebox that
    #asks the user what specfic thing they want from a list of all the
    #things of the type parameter inputed/ of either the all of
    #the tasks or the team members currently.
    specific_choice = choicebox(f"What {type}?", choices=choices) 

    #A if statement that checks if specific choice is None then returns
    #None to stop the function.
    if not specific_choice:
        return 
    
    #The key they specfically picked from the options/choices the user
    #had.
    key = keys[choices.index(specific_choice)]

    #Returning a tuple with the key then exactly what the choice was
    #called that they picked then a list of all the choices they had 
    #to pick from.
    return key, specific_choice, choices
    

def find():
    '''This function displays the a specfic key either from the tasks
    or team member dictionary'''

    #This variable saves the users choice of what type is the thing you
    #are trying to look for from these two options, Task or Team member,
    #by using a buttonbox.
    type = buttonbox("What is the type you want to look into?", \
                     choices  = ["Task","Team member"])
    
    #A if statement that checks if the type variable is None then 
    #returns None to stop the function.
    if not type:
        return 
    
    #The choice varible is the tuple returned by the search function for
    #the type the user picked earlier.
    choice = search(type)

    #A if statement that checks if the choice variable is None then 
    #returns None to stop the function.
    if not choice:
        return choice

    #The message variable is the string returned by the display variable
    #for the type the user pick and their specfic choice for that type.
    #Then the message is displayed in a message box for the user to see.
    message = display(type,choice[0])
    msgbox(message)

    return 


def report():
    '''A function that generates the a report of the amount of tasks
    in each status. It runs a messagebox to show report showing the 
    status and a number representing the amount of tasks on that 
    status.'''

    #A empty string that the message will be appended to.
    message = []

    #A dictionary with keys for every status and value equalling zero to
    #be added to find the amount of tasks in each status.
    status_bins = {
        "Not Started": 0,
        "In Progress" : 0,
        "Blocked" : 0,
        "Completed" : 0,
    
    }

    #A for loop that runs through the all the keys/tasks. Then a nested 
    #for loop that runs through the list of all possible statuses. 
    for task in tasks:
        for status in Status_list:
            
            #if the 'Status' attribute in the task in tasks is equall 
            #to the status variable then that status key in status bins
            #will have one added to it. 
            if tasks[task]["Status"] == status:
                status_bins[status] += 1

    # A for loop that runs through all the keys in the status_bins 
    #dictionary and then appends a f string with the status key and it's
    #value.
    for status_key in status_bins:
        message.append(f"{status_key} - {status_bins[status_key]}")
    
    #This variable just joins all the items of the message list with 
    #two new lines to add space between them and not to print them as a
    #list. 
    final_message = '\n\n'.join(message)
    
    #A msgbox to display the final_message variable.
    msgbox(final_message)

    return 


def task_collection():
    '''This function genererates a list of all the tasks and their 
    details. It displays it in a messsagebox with every task displayed
    with their details indented underneath every task number.'''

    #A variable for the message to get appended to.
    message = ''

    #A for loop that runs through all the keys in the tasks dictionary.
    #Then runs a display function bt inputing the type as "Task" and the
    #keys to get details for each key and then this is added to the 
    #message variable string.
    for key in tasks: 
        message += display("Task",key)

    #A message box displaying the message variable.
    msgbox(message)

    return 


def leave():
    '''This is function is used to when the user click the exit button
    to leave/stop running the program in the main menu.'''

    return 'Exit'

#A dictionary of all the possible options the user has when he is in the
#main menu. The values are the functions that will be called when the 
#user click on a button. The user will see the keys of the dictionary.
options = {
        "New Task":new_task,
        "Find employee or task":find,
        "Update task":update_task,
        "Generate report":report,
        "see task collection":task_collection,
        "Exit":'',
     
    }
#A variable that dictactes if the main program while loop is running 
#when running is true the while loop will continue running when it is 
#set to false the while loop will stop. The while loop runs depending 
#on the value of the running variable.
running = True
while running:
    
    #The message and the title of the main menu buttonbox.
    msg = "What would you like to do?"
    title = "Task Management System"

    #The choices of the user in the main menu which are a list of all
    #the keys in the options dictionary.
    choices = (list(options.keys()))
    
    #The selection variable is what the the user had picked/done in the
    #menu options including exit and closing the program.
    selection = buttonbox(msg,title,choices)
    
    #This if statement checks if selection is an option in the options
    #dictionary. Otherwise then the else statement runs.
    if not options.get(selection):
        #If the selection variable does not exist in the options 
        #dictionary then running is set to false. This stops the main
        #loop. This is to not have an error if a key has a empty value.
        running = False

    else:
        #This variable gets the value of the selection ,which is a key,
        #in the options dictionary then calls it as a function. Then
        #the variable saves what is returned by the function.
        user_choice = options[selection]()

        #An if statement to check if the user_choice equals 'Exit' to 
        #and to make running equal false and stop the while loop meaning
        #stopping the program. If this is not true the while loop 
        #continues runnning.
        if user_choice == 'Exit':
            running = False

