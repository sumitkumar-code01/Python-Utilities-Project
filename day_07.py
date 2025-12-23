'''
   Challenge : Terminal-Based Task List Manager

   Create a Python script that allows users to manage a to-do list 
   directly from the terminal.
   
   Features:
   # Allow users to:

       1. Add a new task.
       2. View all tasks.
       3. Marks a task as completed.
       4. Delete a specific task.
       5. Exit the app

    # save all tasks in a text file named 'tasks.txt' so that the list persists
    between runs of the program.
    
    #Display tasks with an index number and a if completed.

'''

import os

# Function to load tasks from the file
def load_tasks():
    tasks = []
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                # Split task name and status (Task|Status)
                parts = line.strip().split("|")
                if len(parts) == 2:
                    tasks.append({"name": parts[0], "done": parts[1] == "True"})
    return tasks

# Function to save tasks to the file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['name']}|{task['done']}\n")

# Main Function to run the app
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TASK MANAGER ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ")

        if choice == '1':
            print("\nYOUR TO-DO LIST:")
            if not tasks:
                print("List is empty!")
            else:
                for index, task in enumerate(tasks, start=1):
                    status = "[✔]" if task["done"] else "[ ]"
                    print(f"{index}. {status} {task['name']}")

        elif choice == '2':
            new_task = input("Enter the task: ")
            tasks.append({"name": new_task, "done": False})
            save_tasks(tasks)
            print("Task added successfully!")

        elif choice == '3':
            if not tasks:
                print("Nothing to mark!")
                continue
            idx = int(input("Enter task number to mark as done: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]["done"] = True
                save_tasks(tasks)
                print("Task marked as completed!")
            else:
                print("Invalid number!")

        elif choice == '4':
            if not tasks:
                print("Nothing to delete!")
                continue
            idx = int(input("Enter task number to delete: ")) - 1
            if 0 <= idx < len(tasks):
                removed = tasks.pop(idx)
                save_tasks(tasks)
                print(f"Deleted: {removed['name']}")
            else:
                print("Invalid number!")

        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()