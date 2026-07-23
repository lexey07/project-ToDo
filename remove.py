import re

from utils import integer_pattern, subtask_number_pattern
from display import show, show_incorrect_input, show_message
from messages import placeholders
from task_list import task_list


# Удалить задачу
def delete():
    if task_list.is_empty():
        show_message(placeholders["enter_task_first"])

    else:
        user_input = input(placeholders["actual_task"])

        if re.fullmatch(integer_pattern, user_input):
            task_number = int(user_input)

            if 1 <= task_number <= task_list.task_count():
                task_list.remove_task(task_number - 1)

            else:
                show_incorrect_input()

        elif re.fullmatch(subtask_number_pattern, user_input):
            task_parts = user_input.split(".")
            task_number = int(task_parts[0])
            subtask_number = int(task_parts[1])

            if 1 <= task_number <= task_list.task_count():
                task = task_list.get_task(task_number - 1)

                if 1 <= subtask_number <= len(task.subtasks):
                    task.remove_subtask(subtask_number - 1)

                else:
                    show_incorrect_input()

            else:
                show_incorrect_input()

        else:
            show_incorrect_input()
