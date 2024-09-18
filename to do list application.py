# To-Do List Application

# Initialize an empty list to store tasks
tasks = []

# Function to display the menu options
def display_menu():
    print("\nTo-Do List Application")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Mark task as done")
    print("4. Update a task")
    print("5. Remove a task")
    print("6. Exit")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['task']} (Status: {'Done' if task['done'] else 'Pending'})")

# Function to add a new task
def add_task():
    task_description = input("Enter the task description: ")
    tasks.append({"task": task_description, "done": False})
    print(f"Task '{task_description}' added!")

# Function to mark a task as done
def mark_task_done():
    view_tasks()
    task_number = int(input("Enter the task number to mark as done: "))
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['done'] = True
        print(f"Task {task_number} marked as done!")
    else:
        print("Invalid task number.")

# Function to update a task
def update_task():
    view_tasks()
    task_number = int(input("Enter the task number to update: "))
    if 0 < task_number <= len(tasks):
        new_description = input("Enter the new task description: ")
        tasks[task_number - 1]['task'] = new_description
        print(f"Task {task_number} updated to '{new_description}'!")
    else:
        print("Invalid task number.")

# Function to remove a task
def remove_task():
    view_tasks()
    task_number = int(input("Enter the task number to remove: "))
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' removed!")
    else:
        print("Invalid task number.")

# Main loop
while True:
    display_menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        update_task()
    elif choice == "5":
        remove_task()
    elif choice == "6":
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid option. Please choose a number between 1 and 6.")
