from add import add_subtasks, add_task
from top import integer_pattern, re
from display import show 
from remove import delete
from marker import select
from messages import main_menu_actions, add_menu_actions, placeholders

def print_main_menu():
    print(main_menu_actions["menu"])

def print_add_menu():
    print(add_menu_actions["menu"])

def add():
    print_add_menu()
    menu_choice_input = input()

    if re.fullmatch(integer_pattern, menu_choice_input):
        menu_choice = int(menu_choice_input)

        if menu_choice == 1:
            add_task()
            show()

        elif menu_choice == 2:
            add_subtasks()
            show()

        else:
            print(placeholders["incorrect_input"])
            
    else:
        print(placeholders["incorrect_input"])

actions = {
        1: add,
        2: select,
        3: delete,
        4: show
    }

# Меню

while True:
    print_main_menu()

    try:
        menu_choice_input = input()
        menu_choice = int(menu_choice_input)

        if menu_choice == 0:
            break

        elif menu_choice in actions:
            actions[menu_choice]()

        else:
            raise ValueError
        
    except ValueError:
        print(placeholders["incorrect_input"])

# Меню 2

# while True:
#     print_main_menu()
#     menu_choice_input = input()

#     if re.fullmatch(pattern, menu_choice_input):
#         menu_choice = int(menu_choice_input)

#         if menu_choice == 0:
#             break

#         elif menu_choice in actions:
#             actions[choose]()

#         else:
#             print(placeholders["incorrect_input"])

#     else:
#         print(placeholders["incorrect_input"])