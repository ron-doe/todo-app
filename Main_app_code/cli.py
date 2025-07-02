from Main_app_code import functions

import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is",now)


while True:
    user_action = input("Type add, show, complete,  edit or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip() + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos, "todos.txt")

    elif user_action.startswith('show'):
        todos = functions.get_todos("todos.txt")

        for index, item in enumerate(todos, start=1):
            """enumerate and capitalizes all to dos"""
            item = item.capitalize()
            item = item.strip('\n')
            print(f"{index}- {item}")

    elif user_action.startswith('edit'):
        try:
            todos = functions.get_todos()

            for index, item in enumerate(todos, start=1):
                """enumerate and capitalizes all to dos"""
                item = item.capitalize()
                item = item.strip('\n')
                print(f"{index}- {item}")

            number = int(input("Enter number of the to_do to edit"))
            number = number - 1

            new_todo = input("Enter new to_do")
            todos[number] = new_todo +'\n'

            functions.write_todos(todos, "todos.txt")
        except ValueError:
            print("To edit, enter a number. Let's go back to the first menu")
            continue

    elif user_action.startswith('complete'):
        try:
            todos = functions.get_todos()

            for index, item in enumerate(todos, start=1):
                """enumerate and capitalizes all to dos"""
                item = item.capitalize()
                item = item.strip('\n')
                print(f"{index}- {item}")

            number = int(input("Enter number of the to_do to complete"))
            number = number - 1
            completed_todo = todos[number].capitalize().strip('\n')

            todos.pop(number)

            functions.write_todos(todos, "todos.txt")

            message = f"To-do {completed_todo} has been completed."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")
print("Bye!")


         




   