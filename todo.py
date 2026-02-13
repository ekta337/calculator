FILENAME = "tasks.txt"
def load_tasks():
    """Load tasks from file into a list"""
    try:
        with open(FILENAME, "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks list into file"""
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    """Display all tasks"""
    if not tasks:
        print("\nNo tasks available.\n")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print()

def add_task(tasks):
    """Add a new task"""
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")

def remove_task(tasks):
    """Remove a task by number"""
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                save_tasks(tasks)
                print(f"Removed task: {removed}\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")

def main():
    tasks = load_tasks()

    while True:
        print("==== TO-DO LIST MENU ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.\n")

if __name__ == "__main__":
    main()
