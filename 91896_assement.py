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
    "JSMd":{
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


def display():
    pass

def new_task():
    input_list = list(tasks["T1"].keys())
    

    output = multenterbox("Task details", "Add Task", input_list)
    print(output)
    tasks.update({output[0]:{
            "Title":output[1],
            "Description":output[2],
            "Assignee":output[3],
            "Today's Ticket sold":output[4]



    }})


def update_task():
    pass

def search():
    pass

def report():
    pass

def task_collection():
    pass

def leave():
    pass

options = {
        "New Task":new_task,
        "search employee or task":search,
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