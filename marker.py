from top import integer_pattern, subtask_number_pattern, tasks, re
from display import show
from messages import placeholders

# Отметить задач

def select():
    if len(tasks) == 0:
        print(placeholders["enter_task_first"])

    else:
        print(placeholders["actual_task"])
        show()
        user_input = input()

        if re.fullmatch(integer_pattern, user_input):
            task_number = int(user_input)

            if 1 <= task_number <= len(tasks):
                task = tasks[task_number - 1]
                task["done"] = not task["done"]

                for subtask in task["subtasks"]:
                    subtask["done"] = task["done"]

            else:
                print(placeholders["incorrect_input"])

        elif re.fullmatch(subtask_number_pattern, user_input):
            task_parts = user_input.split(".")
            task_number = int(task_parts[0])
            subtask_number = int(task_parts[1])

            if 1 <= task_number <= len(tasks):
                task = tasks[task_number - 1]

                if 1 <= subtask_number <= len(task["subtasks"]):
                    subtask = task["subtasks"][subtask_number - 1]
                    subtask["done"] = not subtask["done"]
                    task["done"] = all(subtask["done"] for subtask in task["subtasks"])

                else:
                    print(placeholders["incorrect_input"])

            else:
                print(placeholders["incorrect_input"])
                
        else:
            print(placeholders["incorrect_input"])