print("Напишите цифру")
tasks = []

def Entering_tasks():
    entering_tasks = input()
    while entering_tasks != "стоп":
        
        task = {
                "title": entering_tasks,
                "done": False
            }

        tasks.append(task)
        entering_tasks = input()

def Print_tasks():
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
    
def Select_an_action():
    check_mark = int(input()) 
    if tasks[check_mark-1]["done"] == False:
        tasks[check_mark-1]["done"] = True
    elif tasks[check_mark-1]["done"] == True:
        tasks[check_mark-1]["done"] = False

def Delete_task():
    numbering2 = int(input())
    del tasks[numbering2-1]

while True:
    print("======================================")
    print("1 - Добавить задачу")
    print("2 - Отметить задачу")
    print("3 - Удалить задачу")
    print("4 - Показать список")
    print("0 - Выход")
    print("======================================")
    select_an_action2 = int(input())
    if select_an_action2 == 1:
        print("Напиши свои задачи, чтобы закончить напишите слово 'стоп'")
        Entering_tasks()
        Print_tasks()
    elif select_an_action2 == 2:
        print("Напиши номер задачи, которыъую ты хочешь отметить")
        Select_an_action()
        Print_tasks()
    elif select_an_action2 == 3:
        print("Напиши номер задачи, которую ты хочешь удалить")
        Delete_task()
        Print_tasks()
    elif select_an_action2 == 4:
        print("Действующий список:")
        Print_tasks()
    elif select_an_action2 == 0 or select_an_action2 > 4:
        print("ПОКА")
        break
