from easygui import *
# do  so when task completed then person doesnt have that in theri task list
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

    "No member":{
        "Name":"none",
        "Email":"none",
        "Tasks Assigned":[],

    }
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
    for i in Input_list:
        detail = value_change(i)

        #A while loop that runs while the detail variable is empty and 
        #asks the user to re-input the empty value.
        while not detail:
            return 1
        output.append(detail)

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
    #The task the user has picked.
    chosen_task = search("Task")
    print(chosen_task)
    #The value the user wants to change.
    detail = buttonbox("What do you want to change?", choices = Input_list)
    print(detail)
        
    #Using the value change function the ask the user what them the new
    #value for the detail they want to change.
    changed_value = value_change(detail)
    print(changed_value)
    #If they click cancel it will go back to the menu and not update the
    #detail.
    if not changed_value:
        return 1
    
    #This updates the chosen detail in the chosen task.
    tasks[chosen_task[0]][detail] = changed_value

    if detail == 'Status' and changed_value == 'Completed':
        assignee = tasks[chosen_task[0]]['Assignee']  
        print("Assignee: " + assignee)
        team_members[assignee]["Tasks Assigned"].remove(chosen_task[0])
        tasks[chosen_task[0]]['Asignee'].remove(assignee)
        
 
    return 1

def value_change(i):
    #Makes a list of all possible assigness or the keys of the team
    #member list.
    assignee_list = list(team_members.keys())
    value = ''

    #A while loop that runs while the value string 
    while value == '': 

        if i == "Title" or i == "Description":
            value = enterbox(f"what is the {i}?")

        elif i == "Assignee":
            value = buttonbox(f"Who is the assignee?","Assignee",assignee_list)
        elif i == "Priority":
            value = integerbox(f"What is the priority?","Priority", \
                               lowerbound=1, upperbound=3)

        elif i == "Status":
            value = buttonbox(f"what is the {i}?","Assignee",Status_list)
    
        if value == '':
            msgbox("Value needs to be inputed")

        elif not value:
            print(value)
   
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
            choices.append(tasks[i]["Title"])

    elif type == "Team_member":
        keys = list(team_members.keys())
        for i in team_members:
            choices.append(team_members[i]["Name"])
    
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
    choice = search(type)

    message = display(type,choice[0])
    msgbox(message)

    return 1

def report():
    
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
    message = ''
    for i in tasks: 
        message += display("Task",i)

    msgbox(message)
    return 1

def leave():
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

