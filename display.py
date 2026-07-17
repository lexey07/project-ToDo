from messages import placeholders, main_menu_actions, add_menu_actions
from task_list import task_list

def show_incorrect_input():
    print(placeholders["incorrect_input"])

def show_main_menu():
    print(main_menu_actions["menu"])

def show_add_menu():
    print(add_menu_actions["menu"])

def get_status_symbol(done):
    if done:
        return "☑"

    return "☐"

def get_task_text(task, task_number):
    task_status = get_status_symbol(task.done)

    return f"{task_number} {task_status} {task.title}"

def get_subtask_text(subtask, task_number, subtask_number):
    subtask_status = get_status_symbol(subtask.done)

    return f"     {task_number}.{subtask_number} {subtask_status} {subtask.title}"

def show_task(task, task_number):
    print(get_task_text(task, task_number))

def show_subtasks(task, task_number):
    subtask_number = 0

    for subtask in task.subtasks:
        subtask_number += 1

        print(get_subtask_text(subtask, task_number, subtask_number))


def show():
    print(placeholders["now_list"])
    task_number = 0

    for task in task_list.get_tasks():
        task_number += 1

        show_task(task, task_number)

        if task.subtasks:
            show_subtasks(task, task_number)
