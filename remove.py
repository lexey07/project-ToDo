from top import integer_pattern, tasks, subtask_number_pattern, re
from display import show
from messages import placeholders

# Удалить задачу

def delete():
    if len(tasks) == 0:
        print(placeholders["enter_task_first"])

    else:
        print(placeholders["actual_task"])
        show()
        user_input = input()

        if re.fullmatch(integer_pattern, user_input):
            task_number = int(user_input)

            if 1 <= task_number <= len(tasks):
                del tasks[task_number - 1]

            else:
                print(placeholders["incorrect_input"])

        elif re.fullmatch(subtask_number_pattern, user_input):
            task_parts = user_input.split(".")
            task_number = int(task_parts[0])
            subtask_number = int(task_parts[1])

            if 1 <= task_number <= len(tasks):
                task = tasks[task_number - 1]

                if 1 <= subtask_number <= len(task["subtasks"]):
                    del task["subtasks"][subtask_number - 1]

                else:
                    print(placeholders["incorrect_input"])

            else:
                print(placeholders["incorrect_input"])
                
        else:
            print(placeholders["incorrect_input"])