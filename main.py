import re

print("Напишите цифру")
tasks = []
pattern = r"\d+"

def entering():
    coming = input()
    while coming != "стоп":
        task = {
                "title": coming,
                "done": False
            }
        tasks.append(task)
        coming = input()

def output():
    global new_tasks
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
    
def select():
    check = input()
    if re.fullmatch(pattern, check):
        inspect = int(check)
        if 1 <= inspect <= len(tasks):
            if tasks[inspect-1]["done"] == False:
                tasks[inspect-1]["done"] = True
            elif tasks[inspect-1]["done"] == True:
                tasks[inspect-1]["done"] = False
        else:
            print("Ошибка!")
    else:
        print("Ошибка!")

def delete():
    number = input()
    if re.fullmatch(pattern, number):
        total = int(number)
        if 1 <= total <= len(tasks):
            del tasks[total-1]
        else:
            print("Ошибка!")
    else:
        print("Ошибка!")
    
def point():
    global tasks
    point = input()
    new_tasks = []
    if re.fullmatch(pattern, point):
        indicate = int(point)
        print(f"Введите задачи (для окончания введите 'стоп')")
        new_com = input()
        while new_com != "стоп":
            new_task = {
                    "title": new_com,
                    "done": False
                }
            new_tasks.insert(0, new_task)
            if len(new_tasks) > indicate:
                new_tasks.pop()
            new_com = input()
    else:
        print("Ошибка!")
    tasks = new_tasks + tasks

while True:
    print("======================================")
    print("1 - Добавить задачу")
    print("2 - Отметить задачу")
    print("3 - Удалить задачу")
    print("4 - Показать список")
    print("5 - Новая функция")
    print("0 - Выход")
    print("======================================")

    pick = input()
    if re.fullmatch(pattern, pick):
        choose = int(pick)
        if choose == 1:
            print("Напиши свои задачи, чтобы закончить напишите слово 'стоп'")
            entering()
            output()
        elif choose == 2:
            print("Напишите номер задачи, которую хотите отметить")
            select()
            output()
        elif choose == 3:
            print("Напишите номер задачи, которую хотите удалить")
            delete()
            output()
        elif choose == 4:
            print("Действующий список:")
            output()
        elif choose == 5:
            print("Введите количество задач, которые хотите написать")
            point()
            output()
        else:
            print("Ошибка! Пока!")
            break
        