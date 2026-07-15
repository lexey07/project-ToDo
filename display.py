from top import tasks
from messages import placeholders

# Нумерация задач

def show():
    print(placeholders["now_list"])
    task_number = 0
    task_status = 0

    for task in tasks:
        task_number += 1

        if task["done"] == False:
            task_status = "☐"

        else:
            task_status = "☑"

        print(task_number, end=" ")
        print(task_status, end=" ")
        print(task["title"])

        if task["subtasks"]:
            subtask_status = 0
            subtask_number = 0

            for subtask in task["subtasks"]:
                subtask_number += 1

                if subtask["done"] == False:
                    subtask_status = "☐"

                else:
                    subtask_status = "☑"

                print(f"     {task_number}.{subtask_number}", end=" ")
                print(subtask_status, end=" ")
                print(subtask["title"])