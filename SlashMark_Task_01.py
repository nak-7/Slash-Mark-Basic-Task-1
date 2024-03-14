#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Define an empty list to store tasks with additional fields
tasks = []

# Emojis for different task statuses and priorities
emojis = {
  "completed": "✅",
  "not_completed": "☑️",
  "high": "❗️",
  "normal": "➖",
  "low": ""
}

# Function to display the to-do list
def display_tasks():
  if not tasks:
    print("Your to-do list is empty.")
  else:
    print("To-Do List:")
    for i, task in enumerate(tasks, start=1):
      status = emojis["completed"] if task["completed"] else emojis["not_completed"]
      priority = task.get("priority", "Normal")  # Default priority if not set
      due_date = task.get("due_date", None)  # Due date can be None
      print(f"{i}. {status} {task['task']} ({priority}, Due: {due_date})")

# Function to add a task to the to-do list
def add_task(task_name, priority="Normal", due_date=None):
  task = {"task": task_name, "completed": False, "priority": priority, "due_date": due_date}
  tasks.append(task)
  print(f"{emojis['not_completed']} Task '{task_name}' added to your to-do list.")

# Function to mark a task as completed
def mark_completed(task_number):
  if 1 <= task_number <= len(tasks):
    tasks[task_number - 1]["completed"] = True
    print(f"{emojis['completed']} Task {task_number} marked as completed.")
  else:
    print("Invalid task number. Please enter a valid task number.")

# Function to remove a task from the to-do list
def remove_task(task_number):
  if 1 <= task_number <= len(tasks):
    removed_task = tasks.pop(task_number - 1)
    print(f"{emojis['completed']} Task '{removed_task['task']}' removed from your to-do list.")
  else:
    print("Invalid task number. Please enter a valid task number.")

# Function to edit a task
def edit_task(task_number):
  if 1 <= task_number <= len(tasks):
    task = tasks[task_number - 1]
    new_task_name = input("Enter new task name (leave blank to keep current): ")
    new_priority = input("Enter new priority (High, Normal, Low): ")
    new_due_date = input("Enter new due date (YYYY-MM-DD format, or leave blank): ")

    if new_task_name:
      task["task"] = new_task_name
    if new_priority:
      task["priority"] = new_priority
    if new_due_date:
      task["due_date"] = new_due_date
    print(f"{emojis['completed']} Task {task_number} edited successfully.")
  else:
    print("Invalid task number. Please enter a valid task number.")
    
def sort_tasks(sort_by="priority"):
  """
  Sorts the tasks list based on the specified criteria.

  Args:
      sort_by (str, optional): The criteria to sort by. Defaults to "priority".
          Can be "priority", "due_date", or "task" (alphabetical).
  """
  if sort_by not in ("priority", "due_date", "task"):
    print("Invalid sort criteria. Please choose 'priority', 'due_date', or 'task'.")
    return

  if sort_by == "priority":
    tasks.sort(key=lambda task: task.get("priority", "normal"))  # Sort by priority
  elif sort_by == "due_date":
    tasks.sort(key=lambda task: task.get("due_date", None))  # Sort by due date (None goes to end)
  elif sort_by == "task":
    tasks.sort(key=lambda task: task["task"].lower())  # Sort by task name (case-insensitive)
    

# Main program loop
while True:
  print("\nOptions:")
  print("1. Display to-do list ")  # Added emoji to option 1
  print("2. Add a task ➕")  # Added emoji to option 2
  print("3. Mark a task as completed ✅")  # Added emoji to option 3
  print("4. Remove a task ➖")  # Added emoji to option 4
  print("5. Edit a task ")  # Added emoji to option 5
  print("6. Sort tasks ")# Added emoji to option 6
  print("7. Exit")#Exit the task
  choice = input("Enter your choice: ")

  if choice == '1':
    display_tasks()
  elif choice == '2':
    task_name = input("Enter the task: ")
    priority = input("Enter priority (High, Normal, Low): ")
    due_date = input("Enter due date (YYYY-MM-DD format, or leave blank): ")
    add_task(task_name, priority.upper(), due_date)
  elif choice == '3':
    display_tasks()
    task_number = int(input("Enter the task number to mark as completed: "))
    mark_completed(task_number)
  elif choice == '4':
    display_tasks()
    task_number = int(input("Enter the task number to remove: "))
    remove_task(task_number)
  elif choice == '5':
    display_tasks()
    task_number = int(input("Enter the task number to edit: "))
    edit_task(task_number)
  elif choice == '6':
    sort_by = input("Sort by (priority, due_date, or task): ")
    sort_tasks(sort_by)
  elif choice == '7':
    print("Exiting To-Do List App. Goodbye!")
    break
  else:
    print("Invalid choice. Please enter a number between 1 and 7.")


# In[ ]:




