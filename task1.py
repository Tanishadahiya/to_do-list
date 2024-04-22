class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
        else:
            print("Invalid task index!")

    def remove_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task["completed"]]

    def display_tasks(self):
        print("TO DO LIST:")
        for i, task in enumerate(self.tasks):
            status = "Completed" if task["completed"] else "you have not completed the task yet"
            print(f"{i + 1}. {task['task']} - {status}")

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add the Task you wanna complete \n press the button 1 to ADD \n")
        print("2. Mark your Task status as Completed \n press the button 2 to MARK COMPLETE \n")
        print("3. Remove your  Completed Tasks \n press the button 3 to REMOVE \n")
        print("4. Display your Tasks that is completed \n press the button 4 to DISPLAY\n")
        print("5. you wanna exit ! \n press the button 5 to EXIT \n")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task you want to complete: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter the index of task to mark as completed: ")) - 1
            todo_list.mark_completed(index)
        elif choice == "3":
            todo_list.remove_completed_tasks()
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("This is a Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
