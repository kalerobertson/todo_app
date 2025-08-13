"""
Simple To-Do List Application
Author: Your Name
Description: A command-line Python app to manage tasks
"""

# Storage for tasks
tasks = []

def display_menu():
    """Display the main menu options."""
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")
    print("===========================\n")

def add_task():
    """Add a new task to the list."""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added!")
    else:
        print("Task cannot be empty!")

def view_tasks():
    """Display all tasks."""
    if not tasks:
        print("No tasks to show!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task():
    """Delete a task by its number."""
    if not tasks:
        print("No tasks to delete!")
        return

    view_tasks()
    try:
        choice = int(input("Enter the number of the task to delete: "))
        if 1 <= choice <= len(tasks):
            removed_task = tasks.pop(choice - 1)
            print(f"Task '{removed_task}' deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main application loop."""
    print("Welcome to the To-Do List App!")

    while True:
        display_menu()
        try:
            option = int(input("Choose an option (1-4): "))
            if option == 1:
                add_task()
            elif option == 2:
                view_tasks()
            elif option == 3:
                delete_task()
            elif option == 4:
                print("Goodbye! Thanks for using the app.")
                break
            else:
                print("Invalid choice. Please enter 1-4.")
        except ValueError:
            print("Please enter a number between 1 and 4.")
        finally:
            print("-" * 30)

if __name__ == "__main__":
    main()
