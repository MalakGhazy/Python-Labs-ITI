from utils import load_data,save_data
from datetime import datetime

PROJECT_FILE = "projects.json"

def create_project(user_email):
    projects = load_data(PROJECT_FILE)
    title = input("Enter Project Title: ").strip()
    details = input("Enter Project Details: ").strip()
    target = input("Enter Project Target (EGP): ").strip()
    start_date = input("Enter Start Date (YYYY-MM-DD): ")
    end_date = input("Enter End Date (YYYY-MM-DD): ")

    if not target.isdigit() or int(target) <= 0:
        print("Invalid target amount!")
        return
    target = int(target)

    try:
        datetime.strptime(start_date,"%Y-%m-%d")
        datetime.strptime(end_date,"%Y-%m-%d")
    except ValueError:
        print("Invalid Date Format!")
        return
    
    if start_date > end_date:
        print("End date must be after start date!")
        return


    project = {
        "id": len(projects) + 1,
        "owner": user_email,
        "title": title,
        "details": details,
        "target": target,
        "start_date": start_date,
        "end_date": end_date
    }   
    projects.append(project)
    save_data(PROJECT_FILE,projects)
    print("Project Created Successfully!")

def view_projects():
    projects = load_data(PROJECT_FILE)       
    for p in projects:
        print(f"{p['id']}. {p['title']} - {p['target']} EGP (From {p['start_date']} to {p['end_date']})")

def edit_project(user_email):
    projects = load_data(PROJECT_FILE)
    project_id = input("Enter project ID to edit: ").strip()
    if not project_id.isdigit():
        print("Invalid project ID!")
        return
    project_id = int(project_id)
    
    for project in projects:
        if project["id"] == project_id and project["owner"] == user_email:
            new_title = input("Enter new title (press Enter to keep current): ").strip()
            new_details = input("Enter new details (press Enter to keep current): ").strip()
            new_target = input("Enter new total target (EGP): ").strip()

            # Validate and convert new_target to an integer if provided
            if new_target:
                if not new_target.isdigit() or int(new_target) <= 0:
                    print("Invalid target amount!")
                    return
                project["target"] = int(new_target)  # Ensure it's stor

            project["title"] = new_title if new_title else project["title"]
            project["details"] = new_details if new_details else project["details"]

            save_data(PROJECT_FILE, projects)
            print("Project updated successfully!")
            return
    print("Project not found or unauthorized access!")

def delete_project(user_email):
    projects = load_data(PROJECT_FILE)
    project_id = input("Enter project ID to delete: ").strip()  # Keep input as a string

    if not project_id.isdigit():  # Validate before converting
        print("Invalid project ID!")
        return
    
    project_id = int(project_id)  # Convert after validation

    new_projects = [p for p in projects if not (p["id"] == project_id and p["owner"] == user_email)]
    
    if len(new_projects) == len(projects):  # If no project was deleted
        print("Project not found or unauthorized access!")
        return
    
    # Renumber remaining projects
    new_projects = [{**p, "id": i + 1} for i, p in enumerate(new_projects)]

    save_data(PROJECT_FILE, new_projects)
    print("Project deleted successfully!")

def search_project():
    date = input("Enter date (YYYY-MM-DD) to search for projects: ").strip()
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Use YYYY-MM-DD")
        return

    projects = load_data(PROJECT_FILE)
    found_projects = [p for p in projects if p["start_date"] <= date <= p["end_date"]]

    if found_projects:
        for p in found_projects:
            print(f"{p['id']}. {p['title']} - {p['target']} EGP (From {p['start_date']} to {p['end_date']})")
    else:
        print("No projects found on this date.")

def project_menu(user_email):
    while True:
        print("\n1. Create Project")
        print("2. View Projects")
        print("3. Edit Project")
        print("4. Delete Project")
        print("5. Search Project")
        print("6. Logout")

        option = input("Choose an option: ")

        if option == "1":
            create_project(user_email)
        elif option == "2":
            view_projects()
        elif option == "3":
            edit_project(user_email)
        elif option == "4":
            delete_project(user_email)
        elif option == "5":
            search_project()
        elif option == "6":
            break
        else:
            print("Invalid option! Please choose a valid number.")

