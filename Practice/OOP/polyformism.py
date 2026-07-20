"""
Полиформизм:

Позволяет применять один и те же команды к объектам разных классов,
даже если они выполняются по-разному.
"""
class Cat():
    def sleep(self):
        print("Спит на полу")

class Bird():
    def sleep(self):
        print("Спит в воздухе")


"""
Метод, который ожидает, что ему на вход придёт объект,
у которого будет метод 'sleep'.
"""
def Sleep(animal):
    animal.sleep()

cat = Cat()
bird = Bird()

Sleep(cat)
Sleep(bird)