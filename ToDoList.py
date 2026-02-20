import os
from datetime import datetime

class Task():
    def __init__(self, task, timetaken, timestamp):
        self.task = task
        self.timetaken = timetaken
        self.timestamp = timestamp

    def __str__(self):
        return f"Task: {self.task}, Time taken: {self.timetaken},{self.timestamp}"
    
    def to_csv(self):
        return f"{self.task},{self.timetaken},{self.timestamp}"
    

tasks = []
filename = "tasks.csv"

if os.path.exists(filename):
    with open(filename,"r") as f:
        for line in f:
            if line.strip():
                task_name, timetaken, timestamp = [x.strip() for x in line.strip().split(",")]
                task = Task(task_name, int(timetaken), timestamp)
                tasks.append(task)
    
else:
    print("No tasks recorded yet.")
    

def add_task():
    task_name = input("Enter task: ").strip()
    timetaken = int(input("Enter time taken for task (Minutes): "))
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")

    task = Task(task_name, int(timetaken), timestamp)
    tasks.append(task)

    with open(filename, "a") as f:
        f.write(task.to_csv()+"\n")

def view_tasks():
    if not tasks:
        print("No tasks recorded.")
        return
    for t in tasks:
        print(t)
        print()

def search_tasks():
    search = input("Enter task to search: ").strip().lower()

    matches = [t for t in tasks if search in t.task.lower()]

    if not matches:
        print("No results for your search.")
        return
    
    else:
        for t in matches:
            print(t)
        
def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return

    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t}")
    
    try:
        choice = int(input("Enter number to delete: ").strip())
        index = choice - 1

        deleted_task = tasks.pop(index)
        print(f"Deleted task: {deleted_task.task}")

        with open(filename, "w") as f:
            for t in tasks:
                f.write(t.to_csv() + "\n")
    
    except (ValueError, IndexError):
        print("Invalid selection.")

def edit_task():
    if not tasks:
        print("No tasks to edit...")
        return
    
    for i, t in enumerate(tasks, start = 1):
        print(f"{i}. {t}")
    
    choice = int(input("Enter number of task to edit: ").strip())
    index = choice - 1

    t = tasks[index]
    
    print("You have selected: ", t)

    new_name = input(f"New task name: (Enter to keep '{t.task}'): ").strip()
    new_minutes = input(f"New minutes (Enter to keep '{t.timetaken}'): ").strip()

    if new_name:
        t.task = new_name
    
    if new_minutes:
        t.timetaken = int(new_minutes)

    print("Updated task: ",t)

    with open(filename, "w", encoding="utf-8") as f:
        for item in tasks:
            f.write(item.to_csv()+"\n")

    print("Saved.")
    


def menu():
    while True:
        print("1. ADD TASK")
        print("2: VIEW TASKS")
        print("3: SEARCH TASK")
        print("4: DELETE TASK")
        print("5: EDIT TASK")
        print("6: EXIT MENU")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            search_tasks()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            edit_task()
        elif choice == "6":
            print("Menu closing...")
            break
        else:
            print("INVALID CHOICE")
        

menu()