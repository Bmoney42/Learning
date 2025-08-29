import os 
import sys
todo = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')   # Windows vs Mac/Linux

while True:
    print("\nWhat Would You Like To Do")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Quit\n")
    user_input = input("Enter Your Choice: ")

    if user_input.isdigit():
        choice = int(user_input)

        if choice == 1:
            clear_screen()
            task = input("Enter New Task ")
            todo.append(task)
            print(f"Added: {task}")
            
        elif choice == 2:
            clear_screen()
            task = input("Which Task Do You Want To Remove ")
            todo.remove(task)
            print(f"Remove: {task}")
            
        elif choice == 3:
            clear_screen()
            for t in todo: 
                print(t)
                
        elif choice == 4:
            sys.exit()
            
