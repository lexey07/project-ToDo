import re

from utils import integer_pattern, subtask_number_pattern
from display import show, show_incorrect_input
from messages import placeholders
from task_list import task_list

# Отметить задач


def select():
    if task_list.is_empty():
        print(placeholders["enter_task_first"])

    else:
        show()
        user_input = input(placeholders["actual_task"])

        if re.fullmatch(integer_pattern, user_input):
            task_number = int(user_input)

            if 1 <= task_number <= task_list.task_count():
                task = task_list.get_task(task_number - 1)
                task.toggle_done()

            else:
                show_incorrect_input()

        elif re.fullmatch(subtask_number_pattern, user_input):
            task_parts = user_input.split(".")
            task_number = int(task_parts[1])
            subtask_number = int(task_parts[1])

            if 1 <= task_number <= task_list.task_count:
                task = task_list.get_task(task_number - 1)

                if 1 <= subtask_number <= len(task.subtasks):
                    task.toggle_subtask(subtask_number - 1)

                else:
                    show_incorrect_input()

            else:
                show_incorrect_input()

        else:
            show_incorrect_input()
