# To-Do List Project
# Student Project

tasks = []

while True:

    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        task = input("Enter your task: ")
        tasks.append(task)

        print("Task Added")

    elif choice == "2":

        print("\nTasks:")

        for task in tasks:
            print(task)

    elif choice == "3":

        print("Thank You")
        break

    else:

        print("Invalid Choice")