import sqlite3
import csv
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Connect to SQLite database
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Create tasks table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        name TEXT,
        completed BOOLEAN
    )
''')
conn.commit()

# Function to validate task name
def validate_task_name(task_name):
    # Validate that the task name is not empty
    if not task_name.strip():
        print(Fore.RED + "Task name cannot be empty.")
        return False
    return True

# Function to execute a query and commit changes
def execute_and_commit(query, *params):
    cursor.execute(query, params)
    conn.commit()

# Function to add a new task
def add_task():
    task_name = input("Enter the task name: ")

    # Validate task name
    if validate_task_name(task_name):
        execute_and_commit("INSERT INTO tasks (name, completed) VALUES (?, ?)", task_name, False)
        print("Task added successfully.")

# Function to edit an existing task
def edit_task():
    view_tasks()

    try:
        task_index = int(input("Enter the index of the task to edit: ")) - 1
        task = cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_index + 1,)).fetchone()

        if task:
            new_name = input(f"Enter the new name for task '{task[1]}': ")

            # Validate the new task name
            if validate_task_name(new_name):
                execute_and_commit("UPDATE tasks SET name = ? WHERE id = ?", new_name, task[0])
                print("Task edited successfully.")
        else:
            print("Invalid task index. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Function to mark a task as completed or incomplete
def mark_task_completed(completed):
    view_tasks()

    try:
        task_index = int(input(f"Enter the index of the task to mark as {'completed' if completed else 'incomplete'}: ")) - 1
        execute_and_commit("UPDATE tasks SET completed = ? WHERE id = ?", completed, task_index + 1)
        print(f"Task marked as {'completed' if completed else 'incomplete'}.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Function to mark a task as completed
def mark_completed():
    mark_task_completed(True)

# Function to mark a task as incomplete
def mark_incomplete():
    mark_task_completed(False)

# Function to view tasks
def view_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    if not tasks:
        print(Fore.YELLOW + "No tasks available.")
    else:
        print("\nTasks:")
        for task in tasks:
            status = Fore.GREEN + "[X]" if task[2] else Fore.RED + "[ ]"
            print(f"{task[0]}. {status} {task[1]}")

        total_tasks = len(tasks)
        completed_tasks = sum(1 for task in tasks if task[2])
        incomplete_tasks = total_tasks - completed_tasks

        print(f"\nTotal tasks: {total_tasks}")
        print(f"Completed tasks: {completed_tasks}")
        print(f"Incomplete tasks: {incomplete_tasks}")

# Function to delete a task
def delete_task():
    view_tasks()

    try:
        task_index = int(input("Enter the index of the task to delete: ")) - 1
        execute_and_commit("DELETE FROM tasks WHERE id = ?", task_index + 1)
        print("Task deleted successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Function to export tasks to a CSV file
def export_to_csv():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    if not tasks:
        print(Fore.YELLOW + "No tasks available to export.")
        return

    try:
        file_name = input("Enter the CSV file name (default: tasks_export.csv): ") or "tasks_export.csv"

        with open(file_name, mode='w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            # Write header
            csv_writer.writerow(["ID", "Task Name", "Status"])
            
            # Write data with 'Completed' or 'Incomplete' instead of boolean values
            for task in tasks:
                status = "Completed" if task[2] else "Incomplete"
                csv_writer.writerow([task[0], task[1], status])

        print(Fore.GREEN + f"Tasks exported to {file_name} successfully!")
    except Exception as e:
        print(Fore.RED + f"Error exporting to CSV: {str(e)}")

# Function to handle main menu options
def main_menu():
    return {
        '1': add_task,
        '2': edit_task,
        '3': mark_completed,
        '4': mark_incomplete,
        '5': view_tasks,
        '6': delete_task,
        '7': export_to_csv,
        '8': exit_program,
    }

# Function to exit the program
def exit_program():
    conn.close()
    print("Exiting Task Manager. Goodbye!")
    exit()
    
# Main function to handle the user interface
def main():
    print("Task Manager")

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Mark Task as Completed")
        print("4. Mark Task as Incomplete")
        print("5. View Tasks")
        print("6. Delete Task")
        print("7. Export to CSV")
        print("8. Exit")

        choice = input("Enter your choice: ")

        # Handle invalid choices
        if choice not in main_menu():
            print(Fore.RED + "Invalid choice. Please try again.")
            continue

        # Execute the chosen function based on user input
        main_menu()[choice]()

        # Check if the user chose to exit
        if choice == '8':
            break  # Exit the loop when '8' is chosen

if __name__ == "__main__":
    main()
