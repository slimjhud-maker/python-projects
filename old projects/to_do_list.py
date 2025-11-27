to_do_list = []

def add_task():
    task = input("Enter the task you would like to add:\n")
    to_do_list.append(task)

def edit_task():
    view_tasks()
    task_num = int(input("Enter the s.no. of the task you would like to edit:\n"))
    if task_num in range(1, len(to_do_list) +1):
        new_task = input("Enter the new task:\n")
        to_do_list[task_num - 1] = new_task 
        print("Task editted successfully")
    else:
        print("Task does not exist")

def view_tasks():
    print("Tasks:\n")
    for i in range (len(to_do_list)):
        print(str(i+1) + ": " + to_do_list[i])

def del_task():
    view_tasks()
    task_num = int(input("Enter the s.no. of the task you would like to mark complete:\n"))
    if task_num in range(1, len(to_do_list) +1):
        del to_do_list[task_num - 1]
        print("Task marked complete")
    else:
        print("Task does not exist")



def main():
    print("To do list:")
    while (True):
        choice = input("\n1: Add a task\n2: Edit a task\n3: View your tasks\n4: Mark complete\n5: Exit\n")
        if choice == "1":
            add_task()
        elif choice == "2":
            edit_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            del_task()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid input")


main()