from easygui import *

#test 1234o432i5oi432[5]
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

def display(type,specific):
    ''' This function is used to display a task or team members full 
    descrition/details. The Function takes in a type parameter which 
    tells the function wheter it needs to display a Task and or
    team member and the specific parameter tells the function what task
    or team memeber specfically to display. The function then creates a
    string variable with the details of the specfic task/team member and
    returns it. '''

    message = ''
    
    if type == "Task":
        
        message += (f"""{specific} :  \nTitle: {tasks[specific]['Title']} \
        \nDescription: {tasks[specific]['Description']}  \
        \nAssignee: {tasks[specific]['Assignee']} \
        \nStatus: {tasks[specific]["Status"]} \n\n""")

    elif type == "Team_member":

        message += (f"""{specific} : \n Name: {team_members[specific]['Name']} \
            \n Email : {team_members[specific]['Email']} \
            \n Tasks Assigned : {team_members[specific]['Tasks Assigned']}""")

    return message

def new_task():

    '''
    This function is run when the user wants to add a new task to the 
    tasks dictionary. Runs through all inputs in a for loop them checks
    if any input is empty and ask for it again 
    
    
    
    
    
    
    '''
    input_list = ["Title","Description","Assignee","Priority","Status"]
    output = []
    task_num = len(list(tasks.keys())) + 1
    output.append(f"T{task_num}")

    for i in input_list:
        detail = value_change(i)
      
        
        while detail == "":
            msgbox("Cannot input empty value")
            detail = value_change(i)#check this

        
        output.append(detail)

    print(output)
    if not output:
        print("works")
    else:
        tasks.update({output[0]:{
            "Title":output[1],
            "Description":output[2],
            "Assignee":output[3],
            "Priority":output[4],
            "Status":output[5]

    }})

    return 1

def update_task():
    input_list = ["Title","Description","Assignee","Priority","Status"]
    
    chosen_task = search("Task")
    print(chosen_task[1])
    value = buttonbox("What do you want to change?", choices = input_list)
    task_num = f"T{chosen_task[1].index(chosen_task[0]) + 1}"
    changed_value = value_change(value)

    tasks[task_num][value] = changed_value

    return 1

def value_change(i):
    assignee_list = list(team_members.keys())
    status_list = ["Not Started","In Progress","Blocked","Completed"]

    if i == "Title" or i == "Description":
        return enterbox(f"what is the {i}?")

    elif i == "Assignee":
        return buttonbox(f"what is the {i}?","Assignee",assignee_list)

    elif i == "Priority":
        return buttonbox(f"what is the {i}?","Assignee",["1","2","3"])

    elif i == "Status":
        return buttonbox(f"what is the {i}?","Assignee",status_list)

        


def search(type):
    choices = []
    if type == "Task":
            
        for i in tasks:
            choices.append(tasks[i]["Title"])

    elif type == "Team_member":
        
        for i in team_members:
            choices.append(team_members[i]["Name"])
    
    specific_choice = choicebox(f"What {type}?", choices=choices)

    return specific_choice , choices
    


def find():
    
    type = buttonbox("What is the type you want to look into?", choices  = ["Task","Team_member"])
    choice = search(type)

    message = display(type,choice)
    msgbox(message)

    return 1

def report():
    status_list = ["Not Started","In Progress","Blocked","Completed"]
    message = []

    status_bins = {
        "Not Started":[],
        "In Progress" : [],
        "Blocked" : [],
        "Completed" : [],
    
    }

    for i in tasks:
        for x in status_list:
            if tasks[i]["Status"] == x:
                status_bins[x].append(f"{i} - {tasks[i]['Title']}")

    
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
    pass

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

