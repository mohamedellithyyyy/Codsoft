# Define an empty list to store tasks
tasks = []

# Function to display tasks
def display_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

# Function to add tasks
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

# Function to remove tasks
def remove_task():
    display_tasks()
    if tasks:
        try:
            idx = int(input("Enter the task number to remove: "))
            if 1 <= idx <= len(tasks):
                removed_task = tasks.pop(idx - 1)
                print(f"Task '{removed_task}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Nothing to remove. Your to-do list is empty.")

# Main loop
while True:
    print("\nOptions:")
    print("1. Display tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting the To-Do List application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
