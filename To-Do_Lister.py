print('''
         ______         ____      
        /_  __/___     / __ \____ 
         / / / __ \   / / / / __ \
        / / / /_/ /  / /_/ / /_/ /
       /_/  \____/  /_____/\____/ 
      / /   (_)____/ /____  _____ 
     / /   / / ___/ __/ _ \/ ___/ 
    / /___/ (__  ) /_/  __/ /     
   /_____/_/____/\__/\___/_/      
                                  
''')

todo_list = []
continue_list = 'y'
while continue_list == 'y':
    action = input("Enter 'a' to add a task and 'd' to delete a task:")
    task = 0
    if action == "a":
        task = input("Enter the task you want to add:")
        todo_list.append(task)
    elif action == "d":
        task = input("Enter the task you want to delete:")
        if task in todo_list:
            todo_list.remove(task)
    print(todo_list)
    continue_list = input("Do you want to add another item to your list? (y/n)")


