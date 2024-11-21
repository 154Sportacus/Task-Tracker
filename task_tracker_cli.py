import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

# Task class to represent individual tasks
class Task:
    def __init__(self, task_id, description, status="todo"):
        self.id = task_id
        self.description = description
        self.status = status
        self.createdAt = datetime.now().isoformat()
        self.updatedAt = self.createdAt

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }

    def update(self, new_description):
        self.description = new_description
        self.updatedAt = datetime.now().isoformat()

    def mark_in_progress(self):
        self.status = "in-progress"
        self.updatedAt = datetime.now().isoformat()

    def mark_done(self):
        self.status = "done"
        self.updatedAt = datetime.now().isoformat()

# TaskManager class to manage the tasks in memory and handle saving/loading
class TaskManager:
    def __init__(self):
        # Ensure the tasks file exists
        if not os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'w') as file:
                file.write('[]')  # Write an empty list as a placeholder
            print(f"{TASKS_FILE} created successfully.")
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from a JSON file into memory."""
        try:
            with open(TASKS_FILE, "r") as file:
                tasks_data = json.load(file)
                tasks = [Task(task_id=task['id'], description=task['description'], status=task['status']) for task in tasks_data]
                return tasks
        except json.JSONDecodeError:
            print(f"Error loading tasks from {TASKS_FILE}. File may be corrupted.")
            return []

    def save_tasks(self):
        """Save all tasks to the JSON file."""
        tasks_data = [task.to_dict() for task in self.tasks]
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks_data, file, indent=4)

    def add_task(self, description):
        """Add a new task to memory and assign it an ID."""
        task_id = len(self.tasks) + 1
        task = Task(task_id, description)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added successfully (ID: {task_id})")

    def update_task(self, task_id, new_description):
        """Update an existing task's description."""
        for task in self.tasks:
            if task.id == task_id:
                task.update(new_description)
                self.save_tasks()
                print(f"Task {task_id} updated successfully")
                return
        print(f"Task with ID {task_id} not found")

    def delete_task(self, task_id):
        """Delete a task by ID."""
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()
        print(f"Task {task_id} deleted successfully")

    def mark_in_progress(self, task_id):
        """Mark a task as 'in-progress'."""
        for task in self.tasks:
            if task.id == task_id:
                task.mark_in_progress()
                self.save_tasks()
                print(f"Task {task_id} marked as in-progress")
                return
        print(f"Task with ID {task_id} not found")

    def mark_done(self, task_id):
        """Mark a task as 'done'."""
        for task in self.tasks:
            if task.id == task_id:
                task.mark_done()
                self.save_tasks()
                print(f"Task {task_id} marked as done")
                return
        print(f"Task with ID {task_id} not found")

    def list_tasks(self, status=None):
        """List tasks by status, or all tasks."""
        tasks = self.tasks if not status else [task for task in self.tasks if task.status == status]
        if tasks:
            for task in tasks:
                print(f"ID: {task.id} | {task.description} | Status: {task.status} | Created: {task.createdAt} | Updated: {task.updatedAt}")
        else:
            print("No tasks found")

# Main function to interact with the user continuously
def main():
    task_manager = TaskManager()

    print("Task Manager CLI")
    print("Type 'quit' to exit.")
    print("Enter command (add, update, delete, mark-in-progress, mark-done, list)")

    while True:
        command = input("\ntask-cli ").strip().lower()
        
        if command == 'quit':
            print("Exiting program.")
            break

        elif command in ["help", "commands"]:
                print("Enter command (add, update, delete, mark-in-progress, mark-done, list, quit)")

        elif command == 'add':
            description = input("Enter task description: ").strip()
            task_manager.add_task(description)

        elif command == 'update':
            task_id = int(input("Enter task ID to update: "))
            new_description = input("Enter new task description: ").strip()
            task_manager.update_task(task_id, new_description)

        elif command == 'delete':
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)

        elif command.startswith('list'):
            parts = command.split()
            if len(parts) == 1:
                status = input("Enter status (todo, in-progress, done) or press enter to list all tasks: ").strip().lower()
            else:
                status = ""
            task_manager.list_tasks(status)

        elif command.startswith('mark-in-progress'):
            parts = command.split()
            if len(parts) == 1:  # No task ID provided
                task_id = int(input("Enter task ID to mark as in-progress: "))
            else:  # Task ID is included in the command
                task_id = int(parts[1])
            task_manager.mark_in_progress(task_id)

        elif command.startswith('mark-done'):
            parts = command.split()
            if len(parts) == 1:  # No task ID provided
                task_id = int(input("Enter task ID to mark as done: "))
            else:  # Task ID is included in the command
                task_id = int(parts[1])
            task_manager.mark_done(task_id)

        else:
            print("Unknown command. Please try again.")

# Start the main function
if __name__ == "__main__":
    main()
