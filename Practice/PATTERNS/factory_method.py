# Factory Method
"""
'ABC' - позволяет создавать абстрактные классы.
'abstactmethod' - позволяет создавать обязательные методы, которые должны быть реализованы в дочерних классах.
"""
from abc import ABC, abstractmethod 

"""
Создается абстрактный класс 'Flowers', который наследуется от 'ABC'. От него будут наследоваться все цветы.
"""
# Продукты
class Flowers(ABC):

    """
    '@abstractmethod' - говорит, что следующий метод является абстрактным и обязан быть реализован в дочернем классе.
    'def smell(self):' - объявляется метод 'smell', который будет отвечать за запах цветов.
    'pass' - пустая реализация метода. Здесь ничего не происходит, потому что метод должен быть переопределен в наследниках.
    """
    @abstractmethod
    def smell(self):
        pass

"""
'class Rose(Flowers):' - создается класс 'Rose', который наследуется от 'Flowers'.
"""
class Rose(Flowers):

    """
    'def smell(self):' - переопределяется метод 'smell' для розы.
    'print("Пахнет розой")' - при вызове метода выводится строка "Пахнет розой".
    """
    def smell(self):
        print("Пахнет розой")

"""
'class Daisies(Flowers):' - создается класс 'daisies', который наследуется от 'Flowers'.
"""
class Daisies(Flowers):

    """
    'def smell(self):' - переопределяется метод 'smell' для ромашек.
    'print("Пахнет ромашкрй")' - при вызове метода выводится строка "Пахнет ромашкой".
    """
    def smell(self):
        print("Пахнет ромашкой")

"""
'class FlowersFactory(ABC):' - создается абстрактная фабрика 'FlowersFactory'.
"""
# Создатель фабрики 
class FlowersFactory(ABC):

    """
    '@abstractmethod' - следующий метод является обязательным для реализации в наследниках.
    'def create_flowers(self) -> Flowers:' - объявляется метод 'create_flowers', который должен вернуть объект типа 'Flowers'.
    'pass' - метод пока не имеет реализации.
    """
    @abstractmethod
    def create_flowers(self) -> Flowers:
        pass

    """
    'def make_smell(self):' - создется обычный метод 'make_smell', который уже полностью реализован.
    'flowers = self.create_flowers()' - вызывается метод 'create_flowers()'. Какая именно реализация будет вызвана, зависит от конкретной
    фабрики. Полученный объект сохраняется в переменную 'flowers'.
    'flowers.smell()' - вызывается метод 'smell' у созданного животного.
    """
    def make_smell(self):
        flowers = self.create_flowers()
        flowers.smell()

"""
'class RoseFactory(FlowersFactory):' - создается фабрика 'RoseFactory', которая наследуется от 'FlowersFactory'.
"""
# Конкретные фабрики
class RoseFactory(FlowersFactory):

    """
    'def create_flowers(self):' - реализуется обязательный метод 'create_flowers'.
    'return Rose()' - создается и возвращается объект класса Rose.
    """
    def create_flowers(self):
        return Rose()

"""
'class DaisiesFactory(FlowersFactory):' - создается фабрика 'DaisiesFactory', которая наследуется от 'FlowersFactory'.
"""
class DaisiesFactory(FlowersFactory):

    """
    'def create_flowers(self):' - реализуется обязательный метод 'create_flowers'.
    'return Daisies()' - создается и возвращается объект класса Daisies.
    """
    def create_flowers(self):
        return Daisies()

"""
'factory = RoseFactory()' - создается объект фабрики 'RoseFActory' и сохраняется в переменную 'factory'.
'factory.make_smell()' - Вызывается метод 'make_smell()'. Внутри него:
                                                        - вызывается 'create_flowers()';
                                                        - создается объект 'Rose()';
                                                        - вызывается 'Rose.smell()';
                                                        - выводится "Пахнет розой".
"""
# Использование
factory = RoseFactory()
factory.make_smell()

"""
'factory = DaisiesFactory()' - создается объект фабрики 'DaisiesFactory' и сохраняется в переменную 'factory'.
'factory.make_smell()' - Вызывается метод 'make_smell()'. Внутри него:
                                                        - вызывается 'create_flowers()';
                                                        - создается объект 'Daisies()';
                                                        - вызывается 'Daisies.smell()';
                                                        - выводится "Пахнет ромашкой".
"""
factory = DaisiesFactory()
factory.make_smell()