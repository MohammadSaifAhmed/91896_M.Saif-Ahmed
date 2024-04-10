from easygui import *
# do  so when task completed then person doesnt have that in theri task list
#do the completed check thing

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
#A list of all the inputs/details of a task
Input_list = ["Title","Description","Assignee","Priority","Status"]

#A list of all the possible status for a task
Status_list = ["Not Started","In Progress","Blocked","Completed"]

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
        
        for x in Input_list:
            message += (f"\n   {x}: {tasks[specific][x]}")

    elif type == "Team_member":
        # A formated string that will formats all the details of the 
        #specific team member put in the parameter of the function.
        
        for details in Member_details:
            message += (f"\n     {details}: {team_members[specific][details]}")

    return message


def assignee_adjust(attribute,value,task):
     if attribute == 'Status' and value == 'Completed':
        assignee = tasks[task]['Assignee']  
        print("Assignee: ", type(assignee))
        if assignee != "None":
            team_members[assignee]["Tasks Assigned"].remove(task)
            print(team_members[assignee]["Tasks Assigned"])
            tasks[task]['Assignee'] = "None"
            
        else:
            pass


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
    task_num = len(list(tasks.keys())) + 1
    output.append(f"T{task_num}")

    #A for loop that runs through all the inputs/details that are needed
    #for the the new task being made and then appends it to the output 
    #list.
    for attribute in Input_list:
        detail = value_change(attribute)
        print(detail)
        #A while loop that runs while the detail variable is empty and 
        #asks the user to re-input the empty value.
        if detail == 1:
            return 1
        output.append(detail)

        assignee_adjust(attribute,detail,output[0])

    #Updates the tasks dictionary witht the new task using the output 
    #list which has all the details.
        
    tasks.update({output[0]:{
        "Title":output[1],
        "Description":output[2],
        "Assignee":output[3],
        "Priority":output[4],
        "Status":output[5]

    }})

    return 1


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

    if chosen_task == 1:
        return 1
    print(chosen_task)
    #The detail/attribute the user wants to change of their choosen 
    #task.
    detail = buttonbox("What do you want to change?", choices = Input_list)
    
    if not detail:
        return 1
        
    #Using the value change function the ask the user what them the new
    #value for the detail they want to change.
    changed_value = value_change(detail)
     
    if changed_value == 1:
        return 1
    print(changed_value)
    #If they click cancel it will go back to the menu and not update the
    #detail.
    if not changed_value:
        return 1
    
    #This updates the chosen detail in the chosen task.
    tasks[chosen_task[0]][detail] = changed_value

    #An if statement that checks if the user has changed the status of 
    #their choosen task and if that choosen task is completed. This to 
    #see if the task needs to be removed from the assignees task list.
    assignee_adjust(detail,changed_value,chosen_task[0])
   
    return 1


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

        #An if statement asks the user for the attribute's value,then
        #saves it in the value variable 
        if attribute == "Title" or attribute == "Description":
            value = enterbox(f"what is the {attribute}?")
        #This elif statement checks if the attrubute is the Assignee. 
        #As the assignee attribute uses a buttonbox with it's own 
        #options list.
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


        if value == '':
            msgbox("Value needs to be inputed")

        elif not value or not attribute:
            return 1
   
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
    choices = []
    
    if type == "Task":
        keys = list(tasks.keys())
        for i in tasks:
            choices.append(f"{i} - {tasks[i]['Title']}")

    elif type == "Team_member":
        keys = list(team_members.keys())
        for i in team_members:
            choices.append(f"{team_members[i]['Name']}")
    
    specific_choice = choicebox(f"What {type}?", choices=choices) 

    if not specific_choice:
        return 1
    key = keys[choices.index(specific_choice)]

    return key, specific_choice, choices
    

def find():
    '''This function displays the a specfic key either from the tasks
    or team member dictionary'''
    type = buttonbox("What is the type you want to look into?", \
                     choices  = ["Task","Team_member"])
    
    if not type:
        return 1
    choice = search(type)

    if choice == 1:
        return choice

    message = display(type,choice[0])
    msgbox(message)

    return 1


def report():
    '''A function that generates the a report of the amount of tasks
    in each status. It runs a messagebox to show report showing the 
    status and a number representing the amount of tasks on that 
    status.'''
    message = []

    status_bins = {
        "Not Started": 0,
        "In Progress" : 0,
        "Blocked" : 0,
        "Completed" : 0,
    
    }

    for i in tasks:
        for x in Status_list:
            if tasks[i]["Status"] == x:
                status_bins[x] += 1

    
    for i in status_bins:
        message.append(f"{i} - {status_bins[i]}")
    

    final_message = '\n\n'.join(message)
    
    msgbox(final_message)

    return 1


def task_collection():
    '''This function genererates a list of all the tasks and their 
    details. It displays it in a messsagebox with every task displayed
    with their details indented underneath every task number.'''
    message = ''
    for i in tasks: 
        message += display("Task",i)

    msgbox(message)
    return 1


def leave():
    '''This is function is used to when the user click the exit button
    to leave/stop running the program in the main menu.'''
    return None


options = {
        "New Task":new_task,
        "Find employee or task":find,
        "Update task":update_task,
        "Generate report":report,
        "see task collection":task_collection,
        "Exit":leave,
     
    }

running = True
while running:
    
    msg = "What would you like to do?"
    title = "Task Management System"

    choices = (list(options.keys()))
    
    selection = buttonbox(msg,title,choices)
    
    if not options.get(selection):
        running = False
    else:
        user_choice = options[selection]()

        if not user_choice:
            running = False

