import csv


class task:
    def __init__(self, name, priority, description):
        self.name = name
        self.priority = priority
        self.description = description
    
    def __str__(self):
        return f"{self.name.upper()} - {self.description.upper()} (Priority: {self.priority.upper()})"
    
    def save_to_dict(self):
        return {"name":self.name.lower(), "priority":self.priority.lower(), "description":self.description.lower()}


class to_do_list:
    def __init__(self):
        self.tasklist=[]

    def add_task(self, task1):
        self.tasklist.append(task1)
        print(f"Task named {task1} was added!")

    def remove_task(self, task1):
        for task2 in self.tasklist:
            if task2.name == task1:
                self.tasklist.remove(task2)
                print(f"Task '{task1}' removed successfully!")
                return
        print(f"Task '{task1}' not found!")
    

    def view_tasks(self):
            if not self.tasklist:
                print("No tasks in the list!")
                return

            print("\nCurrent Tasks:")
            for i, task in enumerate(self.tasklist, 1):
                print(f"{i}. {task}")
            print()
           
    def save_to_csv(self, filename="todo_list.csv"):
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'description', 'priority'])
            writer.writeheader()
            for task in self.tasklist:
                writer.writerow(task.save_to_dict())
        print(f"Tasks saved to {filename} successfully!")
        
    def load_from_csv(self, filename="todo_list.csv"):
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                self.tasklist = []
                for row in reader:
                    self.tasklist.append(task(row['name'], row['description'], row['priority']))
            print(f"Tasks loaded from {filename} successfully!")
        
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty list.")
        except Exception as e:
            print(f"Error loading file: {e}")

#####################

def display_menu():
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Save to CSV")
    print("5. Load from CSV")
    print("6. Exit")
############################
def main():
    todo_list = to_do_list()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            name = input("Enter task name: ").strip()
            description = input("Enter task description: ").strip()
            priority = input("Enter task priority: ")
            task1 = task(name, description, priority)
            todo_list.add_task(task1)
            
        elif choice == '2':
            name = input("Enter task name to remove: ").strip()
            todo_list.remove_task(name)
            
        elif choice == '3':
            todo_list.view_tasks()
            
        elif choice == '4':
            filename = input("Enter filename to save (default: todo_list.csv): ").strip()
            if not filename:
                todo_list.save_to_csv()
            else:
                todo_list.save_to_csv(filename)
                
        elif choice == '5':
            filename = input("Enter filename to load (default: todo_list.csv): ").strip()
            if not filename:
                todo_list.load_from_csv()
            else:
                todo_list.load_from_csv(filename)
                
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()



