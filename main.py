import re
from add import add_subtasks, add_task
from utils import integer_pattern
from display import show, show_main_menu, show_add_menu, show_incorrect_input, show_message
from remove import delete
from marker import select
from messages import placeholders


def add():
    show_add_menu()
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
            show_incorrect_input()

    else:
        show_incorrect_input()


actions = {1: add, 2: select, 3: delete, 4: show}

# Меню
while True:
    show_main_menu()

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
        show_incorrect_input()

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
#             show_incorrect_input()

#     else:
#         show_incorrect_input()
