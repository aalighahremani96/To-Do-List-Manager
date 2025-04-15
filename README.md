# To-Do-List-Manager
This project is part of my Python course assignments. It implements a command-line To-Do List Manager using Object-Oriented Programming (OOP), CSV file handling, and basic data management.

## Project Description

In this project, you will build a To-Do List application with the following features:

- Add new tasks  
- Remove existing tasks  
- View the current list of tasks  
- Save tasks to a CSV file  
- Load tasks from a CSV file  
- Assign priority to each task (High, Medium, or Low)

---

## Project Features

### ✅ Add Task
Add a new task to the list with a name, description, and priority.

### ❌ Remove Task
Delete a task from the list by its name or index.

### 📄 View Tasks
Display all tasks currently in the list.

### 💾 Save to CSV
Automatically save the task list to a CSV file.

### 📂 Load from CSV
Automatically load the task list from a CSV file at program startup.

---

## Project Structure

### 1. `Task` Class
Models a single task with the following attributes:
- `name`: The name/title of the task  
- `description`: A short description of the task  
- `priority`: Task priority (e.g., High, Medium, Low)

### 2. `ToDoList` Class
Handles the task list and operations:
- `add_task(task)`
- `remove_task(task_name)`
- `view_tasks()`
- `save_to_csv(filename)`
- `load_from_csv(filename)`

### 3. Text-Based Menu
The program includes a simple terminal menu for the user to:
- Add new tasks  
- Remove existing tasks  
- View all tasks  
- Save tasks to a file  

---

## Technologies Used
- Python 3.x  
- CSV Module  
- Object-Oriented Programming (OOP)
