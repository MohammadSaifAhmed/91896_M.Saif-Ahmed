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


def display(type,specific):

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
    input_list = ["Title","Description","Assignee","Priority","Status"]
    assignee_list = list(team_members.keys())
    print(type(assignee_list))
    status_list = ["Not started","In Progress","Blocked"]
    output = []
    output.append(f"T{len(tasks)+ 1}")

    for i in input_list:
        print(i)
        if i == "Title" or i == "Description":
            output.append(enterbox(f"what is the {i}?"))

        elif i == "Assignee":
            output.append(buttonbox(f"what is the {i}?","Assignee",assignee_list))

        elif i == "Priority":
            output.append(buttonbox(f"what is the {i}?","Assignee",["1","2","3"]))

        elif i == "Status":
            output.append(buttonbox(f"what is the {i}?","Assignee",status_list))


  


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
    pass

def search(type):
    if type == "Task":
        choices = tasks.keys()

    elif type == "Team_member":
        choices = team_members.keys()

    print(choices)
    specific_choice = choicebox(f"What {type}?", choices=choices)

    return specific_choice



def find():
    
    type = buttonbox("What is the type you want to look into?",choices  = ["Task","Team_member"])
    choice = search(type)

    message = display(type,choice)
    msgbox(message)

    return 1


def report():
    pass

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