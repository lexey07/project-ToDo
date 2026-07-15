from top import tasks, task_count, integer_pattern, re
from display import show
from messages import placeholders

# Ввод задач, под определенное количество. Ввод подзадач

def add_task():
        # print(placeholdres["number"])
        # task_count = input()
        # if re.fullmatch(pattern, task_count):
        #     task_count = int(task_count)
            print(placeholders["enter_tasks"])
            current_task = None
            user_input = input()

            while user_input != "стоп":
                if user_input.startswith("-"):
                    if current_task is None:
                        print(placeholders["enter_task_first"])
                    
                    else:
                        subtask = {
                            "title": user_input,
                            "done": False
                        }

                        current_task["subtasks"].append(subtask)
                
                else:
                    task = {
                        "title": user_input,
                        "done": False,
                        "subtasks": []
                    }     

                    current_task = task

                    if len(tasks) < task_count:
                        tasks.append(task)

                    else:
                        tasks.pop(-1)
                        tasks.insert(0, task)

                user_input = input()

        # else:
        #     print("Ошибка!")
    
# Ввод подзадач

def add_subtasks():
    if len(tasks) == 0:
         print(placeholders["enter_task_first"])

    else:
        print(placeholders["choose_task"])
        show()
        task_number_input = input()

        if re.fullmatch(integer_pattern, task_number_input):
            task_number = int(task_number_input)

            if 1 <= task_number <= len(tasks):
                task = tasks[task_number - 1]
                print(placeholders["enter_subtasks"])
                subtask_input = input()

                while subtask_input != "стоп":
                    subtask = {
                        "title": subtask_input,
                        "done": False
                    }

                    task["subtasks"].append(subtask)
                    subtask_input = input()
            else:
                print(placeholders["incorrect_input"])
                
        else:
            print(placeholders["task_number_only"])