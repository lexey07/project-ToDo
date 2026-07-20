import re

from utils import integer_pattern
from display import show, show_incorrect_input
from messages import placeholders
from task import Task
from task_list import task_list


# Ввод задач, под определенное количество. Ввод подзадач
def add_task():
    current_task = None
    user_input = input(placeholders["enter_tasks"])

    while user_input != "стоп":
        if user_input.startswith("-"):
            if current_task is None:
                print(placeholders["enter_task_first"])

            else:
                subtask = Task(user_input)
                current_task.add_subtask(subtask)

        else:
            task = Task(user_input)
            current_task = task

            task_list.add_task(task)

        user_input = input()

# Ввод подзадач
def add_subtasks():
    if task_list.is_empty():
        print(placeholders["enter_task_first"])

    else:
        print(placeholders["choose_task"])
        show()
        task_number_input = input()

        if re.fullmatch(integer_pattern, task_number_input):
            task_number = int(task_number_input)

            if 1 <= task_number <= task_list.task_count():
                task = task_list.get_task(task_number - 1)                
                print(placeholders["enter_subtasks"])
                subtask_input = input()

                while subtask_input != "стоп":
                    subtask = Task(subtask_input)

                    task.add_subtask(subtask)
                    subtask_input = input()
            else:
                show_incorrect_input()

        else:
            print(placeholders["task_number_only"])
