import re

from utils import integer_pattern
from display import show, show_incorrect_input, show_message
from messages import placeholders
from task import Task
from task_list import task_list

def add_task():
    current_task = None

    for user_input in iter(input, "стоп"): # 'iter(input, "стоп") - замсеняет while и постоянный вызов
        if user_input.startswith("-"):
            if current_task is None:
                show_message(placeholders["enter_task_first"])
            else:
                subtask = Task(user_input)
                current_task.add_subtask(subtask)

        else:
            task = Task(user_input)
            current_task = task

            task_list.add_task(task)

# Ввод подзадач
def add_subtasks():
    if task_list.is_empty():
        show_message(placeholders["enter_task_first"])

    else:
        show_message(placeholders["choose_task"])
        show()
        task_number_input = input()

        if re.fullmatch(integer_pattern, task_number_input):
            task_number = int(task_number_input)

            if 1 <= task_number <= task_list.task_count():
                task = task_list.get_task(task_number - 1)

                show_message(placeholders["enter_subtasks"])

                for subtask_input in iter(input, "стоп"):
                    subtask = Task(subtask_input)
                    task.add_subtask(subtask)

            else:
                show_incorrect_input()

        else:
            show_message(placeholders["task_number_only"])
