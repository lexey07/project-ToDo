import re

print("Напишите цифру")
tasks = []
pattern = r"\d+"
pattern2 = r"\d+\.\d+"
#task_count = 5

# Ввод задач, под определенное количество
def entering():
        print("Введите количество задач, которые хотите добавить")
        task_count = input()
        if re.fullmatch(pattern, task_count):
            task_count = int(task_count)
            print("Введите задачи (Напишите слово 'стоп', чтобы закончить)")
            coming = input()
            while coming != "стоп":
                task = {
                        "title": coming,
                        "done": False,
                        "subtasks": []
                    }
                tasks.insert(0, task)
                coming = input()             
                if len(tasks) > task_count:
                    tasks.pop()
        else:
            print("Ошибка!")
            
# Ввод подзадач
def subentering():
    output()
    print("Выберите задачу, к которой хотите добавить подзадачу")
    subcoming = input()
    if re.fullmatch(pattern, subcoming):
        sub = int(subcoming)
        if 1 <= sub <= len(tasks):
            task = tasks[sub - 1]
            print("Напишите подзадачу(и) (Напишите слово 'стоп', чтобы закончить)")
            coming2 = input()
            while coming2 != "стоп":
                subtasks = {
                    "title": coming2,
                    "done": False
                }
                task["subtasks"].append(subtasks)
                coming2 = input()
        else:
            print("Ошибка!")
    else:
        print("Ошибка!")

# Нумерация задач
def output():
    numbering = 0
    symbol = 0
    for task in tasks:
        numbering += 1
        if task["done"] == False:
            symbol = "☐"
        else:
            symbol = "☑"

        print(numbering, end=" ")
        print(symbol, end=" ")
        print(task["title"])

        if task["subtasks"]:
            task_symbol = 0
            numbering2 = 0
            for subtasks in task["subtasks"]:
                numbering2 += 1
                if subtasks["done"] == False:
                    task_symbol = "☐"
                else:
                    task_symbol = "☑"

                print(f"     {numbering}.{numbering2}", end=" ")
                print(task_symbol, end=" ")
                print(subtasks["title"])


# Отметить задач
def select():
    output()
    print("Напишите номер задачи или подзадачи, которую хотите отметить")
    check = input()
    if re.fullmatch(pattern, check):
        inspect = int(check)
        if 1 <= inspect <= len(tasks):
            task = tasks[inspect - 1]
            task["done"] = not task["done"]
            for subtask in task["subtasks"]:
                subtask["done"] = task["done"]
        else:
            print("Ошибка!")
    elif re.fullmatch(pattern2, check):
        parts = check.split(".")
        task_number = int(parts[0])
        subtasks_number = int(parts[1])
        if 1 <= task_number <= len(tasks):
            task = tasks[task_number - 1]
            if 1 <= subtasks_number <= len(task["subtasks"]):
                subtask = task["subtasks"][subtasks_number - 1]
                subtask["done"] = not subtask["done"]
                task["done"] = all(subtask["done"] for subtask in task["subtasks"])
            else:
                print("Ошибка!")
        else:
            print("Ошибка!")
    else:
        print("Ошибка!")

# Удалить задачу
def delete():
    number = input()
    if re.fullmatch(pattern, number):
        total = int(number)
        if 1 <= total <= len(tasks):
            del tasks[total-1]
        else:
            print("Ошибка!")
    elif re.fullmatch(pattern2, number):
        parts2 = number.split(".")
        index = int(parts2[0])
        index2 = int(parts2[1])
        if 1 <= index <= len(tasks):
            task = tasks[index - 1]
            if 1 <= index2 <= len(task["subtasks"]):
                del task["subtasks"][index2 - 1]
            else:
                print("Ошибка!")
        else:
            print("Ошибка!")
    else:
        print("Ошибка!")

def print_main_menu():
    print("======================================")
    print("1 - Добавить задачу")
    print("2 - Отметить задачу")
    print("3 - Удалить задачу")
    print("4 - Показать список")
    print("0 - Выход")
    print("======================================")

def print_add_menu():
    print("======================================")
    print("1 - Добавить задачу")
    print("2 - Добавить подзадачу")
    print("======================================")

def add():
    print_add_menu()
    pick2 = input()
    if re.fullmatch(pattern, pick2):
        choose2 = int(pick2)
        if choose2 == 1:
            entering()
            output()
        elif choose2 == 2:
            subentering()
            output()
        else:
            print("Напишите номер из предложенных вариантов")
    else:
        print("Ошибка!")

actions = {
        1: add,
        2: select,
        3: delete,
        4: output
    }

# Меню
while True:
    print_main_menu()
    pick = input()
    if re.fullmatch(pattern, pick):
        choose = int(pick)
        if choose == 0:
            break
        elif choose in actions:
            actions[choose]()
        else:
            print("Ошибка!")
    else:
        print("Ошибка!")
        