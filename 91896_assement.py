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



def display(type,specific):
    ''' This function is used to display a task or team members full 
    descrition/details. The Function takes in a type parameter which 
    tells the function wheter it needs to display a Task and or
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
    
    #An if statement which appends to the message depending on if it is
    #in the tasks dictionary or the team member dictionary.
    if type == "Task":
        # A formated string that will formats all the details of the 
        #specific task put in the parameter of the function.
        message += (f"\n{specific} :")
        for x in Input_list:
            message += (f"\n   {x}: {tasks[specific][x]}")

    elif type == "Team_member":
        # A formated string that will formats all the details of the 
        #specific team member put in the parameter of the function.
        
        message += (f"""{specific} : \n  Name: {team_members[specific]['Name']}\
            \n   Email : {team_members[specific]['Email']} \
            \n   Tasks Assigned : {team_members[specific]['Tasks Assigned']}""")

    return message

def new_task():
    ''' This function is run when the user wants to add a new task to 
    the tasks dictionary. It runs through all inputs in a for loop then 
    checks if any input is empty and ask for it again until all value 
    are not empty. '''

    #All the inputs the user will be asked for  vb 
    
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
            msgbox("Cannot input empty value")
            detail = value_change(i)
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
   
    
    chosen_task = search("Task")
    print(chosen_task)
    value = buttonbox("What do you want to change?", choices = Input_list)
    print(value)
   
        
    
    changed_value = value_change(value)
    print(changed_value)
    if not changed_value:
        return 1


    tasks[chosen_task[0]][value] = changed_value
    print(changed_value)
    return 1

def value_change(i):
    assignee_list = list(team_members.keys())
    

    if i == "Title" or i == "Description":
        return enterbox(f"what is the {i}?")

    elif i == "Assignee":
        return buttonbox(f"what is the {i}?","Assignee",assignee_list)

    elif i == "Priority":
        return buttonbox(f"what is the {i}?","Assignee",["1","2","3"])

    elif i == "Status":
        return buttonbox(f"what is the {i}?","Assignee",Status_list)

        
def search(type):
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
    key = keys[choices.index(specific_choice)]

    return key, specific_choice, choices
    


def find():
    
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

