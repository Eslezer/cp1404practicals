"""
CP1404/CP5632 Practical
Program for managing project and details

estimate time: 30 minutes
actual time: 60 minutes
"""

import csv
from project import Project
import datetime

FILENAME = "projects.txt"

def load_projects(filename):
    projects = [] #opens the file
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)
        for row in reader:
            projects.append(Project(*row))
    return projects

def save_projects(filename, projects):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['Name', 'Start Date', 'Priority', 'Cost Estimate', 'Completion Percentage'])
        for project in projects:
            writer.writerow([project.name, project.start_date.strftime('%d/%m/%Y'),
                             project.priority, project.cost_estimate, project.completion_percentage])

def display_projects(projects):
    incomplete = sorted([p for p in projects if not p.is_complete()]) # shows incomplete projects
    completed = sorted([p for p in projects if p.is_complete()]) # shows complete projects
    print("Incomplete projects:") # prints incomplete
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:") # prints complete
    for project in completed:
        print(f"  {project}")

def filter_projects_by_date(projects, date):
    filtered = [p for p in projects if p.start_date > date]
    for project in sorted(filtered, key=lambda p: p.start_date): #key lambda sorts the projects, helps simplify the process shortly
        print(project) #prints projects by date

def add_new_project(projects): #simple function to add a new project
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion = input("Completion percentage: ")
    projects.append(Project(name, start_date, priority, cost_estimate, completion))

def update_project(projects): # function to update the details of project
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    percentage = input("New Percentage: ")
    priority = input("New Priority: ")
    if percentage:
        project.completion_percentage = int(percentage)
    if priority:
        project.priority = int(priority)

def main():
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n" \
           "- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"
    print(MENU) # print the main menu
    choice = input(">>> ").lower() # lets the user choice no matter lower or upper case
    while choice != 'q': # executes the respective function to each command
        if choice == 'l':
            filename = input("Filename to load: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
            filter_projects_by_date(projects, date)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").lower() # reopens the menu if the user doesn't quit with "Q"

    save_choice = input(f"Save changes to {FILENAME}? (y/n) ").lower() # once quit, gives you the option to save before leaving
    if save_choice == 'y':
        save_projects(FILENAME, projects)
        print(f"Projects saved to {FILENAME}")

    print("Thank you for using custom-built project management software.")

main()
