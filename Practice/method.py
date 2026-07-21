list = [1, 'Yellow', 564, 'Tramp']

# Метод append()
list.append('Spanish')
print(list)

# Без метода append()
list = list + ['Spanish']
print(list)

# Метод insert()
list.insert(2, 123)
print(list)

# Без метода insert()
"""I am stupid boy"""
numbers = [1, 2, 4]
index = 2
value = 3
new_list = []

for i in range(index):
    new_list.append(numbers[i])

new_list.append(value)

for i in range(index, len(numbers)):
    new_list.append(numbers[i])

numbers = new_list
print(numbers)


#Метод extend()
list.extend([198, 'May', 'Harry Potter'])
print(list)

# Без метода extend()
list = list + [198, 'May', 'Harry Potter']
print(list)

# Метод remove()
list.remove(198)
print(list)

# Без метода remove()
"""I am stupid boy"""
numbers = [1, 2, 3, 2]
new_list = []
deleted = False

for item in numbers:
    if item == 2 and not deleted:
        deleted = True
        continue

    new_list.append(item)
numbers = new_list
print(numbers)

# Метод pop()
list.pop(2)
print(list)

# Без метода pop()
if list[2] in list:
    del list[2]
    print(list)

# Метод clear()
# list.clear()
# print(list)

# # Без метода clear()
# del list
# list = []
# print(list)

# Метод index()
print(list.index('Tramp'))

# Без метода index()
for i in range(len(list)):
    if list[i] == 'Tramp':
        result = i
        print(i)
        break

# Метод count()
print(list.count('May'))

# Без метода count()
n = 0
for i in list:
    if i == 'May':
        n += 1
print(n)

# Метод sort()
new_list = [1, 2, 6, 5, 4, 67]
new_list.sort()
print(new_list)

# Без метода sort()
for i in range(len(new_list)):
    for j in range(len(new_list) - i - 1):
        if new_list[j] > new_list[j + 1]:
            new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]

print(new_list)

# Метод reverse()
old_list = [1, 7, 98, 'Dra']
old_list.reverse()
print(old_list)

# Без метода reverse()
new_list1 = []
index = len(old_list)
for i in range(index - 1, -1, -1):
    new_list1.append(old_list[i])

old_list = new_list1

print(old_list)

# Метод copy()
new_old_list = old_list.copy()
print(new_old_list)

#Без метода copy()
new_new_list = []
new_new_list.append(old_list)
print(new_new_list)