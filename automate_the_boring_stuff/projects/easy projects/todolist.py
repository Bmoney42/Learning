#

todo = []

While True:
  print("\nWhat Would You Like To Do")
  print("1. Add Task")
  print("2. Remove Task")
  print("3. Show Tasks")
  print("4. Quit")
  choice = input("Enter Your Choice")

if choice == 1:
  task = input("Enter New Task")
  todo.append(task)
  print(f"Added: {task}")

if choice == 2:
  task = input("Which Task Do You Want To Remove")
  todo.remove(task)
  print(f"Remove: {task}")




