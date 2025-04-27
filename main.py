
#from functions import get_todos , write_todos
import functions
import time
time.strftime('%b %d, %Y,  ')
while True:
    #get user input and strip space chars from it
    user_action = input("Type add, show, edit  or show:")
    user_action = user_action.strip()#metodo strip quita los espacios

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()


            new_todo = input('enter a new todo')
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print('your command is not valid')
            continue


    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f'Todo {todo_to_remove} was removed from the list'
            print(message)
        except IndexError:
            print('there is no item with that number')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('comand not rigth')#esto es un metodo
print('bye!')
#metodos son funciones preprogramas de pyton
#append es para indexar una lista
#  y se empieze a acumular



