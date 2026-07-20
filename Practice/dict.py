# Словарь
students = {
    "245637": "Иванов Иван Иванович",
    "123645": "Артемов Артем Артемович",
    "039463": "Максимов Максим Максимович"
}

students["466838"] = "Николаев Николай Николаевич" # Добавляем новый эелемент в словарь

bad_student = students["245637"] # Достаем значение ключа из словаря

del students["123645"] # Удаляем элемент из словаря

students["039463"] = "Олегов Олег Олегович" # Изменяем значение ключа в словаре

# Метод 'update()' - добавляет в словарь одну или сразу несколько пар "ключ - значение"
students.update({
    "657048": "Петров Петр Петрович",
    "897624": "Павлов Павел Павлович"
})

# Метод 'get()' - возвращает значение из словаря по ключу или 'None', если такого ключа не существует
good_students = students.get("657048")
not_good_students = students.get("564739", "К сожалению, такого ключа нет(")

# Метод 'pop()' - удаляет элемемент из словаря по ключу
expelled = students.pop("466838")

# Метод 'keys()' - возвращает все ключи из словаря — но без значений
students_keys = students.keys()

# Метод 'values()' - возвращает все значения из словаря — но без ключей
students_values = students.values()

# Метод 'items()' - возвращает все пары «ключ — значение»
students_items = students.items()

# Метод 'clear()' - удаляет все из словаря
students_clear = students.clear()

# Метод 'copy()' - создает копию словаря
students_copy = students.copy()

# Метод 'popitem()' - удаляет последнюю добавляенную пару "ключ - значение"
students_popitem = students.popitem()

# Метод 'setdefault()' - Возвращает значение указанного ключа. Если ключа не существует, 
# создаёт его и добавляет в словарь со значением "None" или тем, что вы добавите в качестве второго аргумента
students_setdafault = students.setdefault("345722", "Андреев Андрей Андреевич")

print(students)
# print(students_keys)
# print(students_values)
# print(students_items)
# print(students_clear) # None
# print(students_copy)
# print(students_popitem) # ('897624', 'Павлов Павел Павлович')
# print(students_setdafault) # Андреев Андрей Андреевич
# print(expelled) # Николаев Николай Николаевич
# print(good_students) # Петров Петр Петрович
# print(not_good_students) # 'None' или свое значение (пишется вторым аргументом)
# print(bad_students) # Иванов Иван Иванович