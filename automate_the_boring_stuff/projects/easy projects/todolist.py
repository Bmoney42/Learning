import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def prompt_choice():
    print("\nWhat Would You Like To Do")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Quit")
    user_input = input("Enter Your Choice: ").strip()
    return int(user_input) if user_input.isdigit() else None

def add_task(todo):
    clear_screen()
    task = input("Enter New Task: ").strip()
    if task:
        todo.append(task)
        print(f"Added: {task}")
    input("\nPress Enter to continue...")

def remove_task(todo):
    clear_screen()
    if not todo:
        print("No tasks to remove.")
        input("\nPress Enter to continue...")
        return
    for i, t in enumerate(todo, start=1):
        print(f"{i}. {t}")
    pick = input("\nEnter number to remove (or Enter to cancel): ").strip()
    if pick.isdigit():
        i = int(pick) - 1
        if 0 <= i < len(todo):
            removed = todo.pop(i)
            print(f"Removed: {removed}")
    input("\nPress Enter to continue...")

def show_tasks(todo):
    clear_screen()
    if not todo:
        print("No tasks yet!")
    else:
        for i, t in enumerate(todo, start=1):
            print(f"{i}. {t}")
    input("\nPress Enter to continue...")

def main():
    todo = []
    actions = {
        1: lambda: add_task(todo),
        2: lambda: remove_task(todo),
        3: lambda: show_tasks(todo),
        4: lambda: exit(0),
    }
    while True:
        clear_screen()
        choice = prompt_choice()
        action = actions.get(choice)
        if action:
            action()
        else:
            print("\nInvalid choice. Try 1-4.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
