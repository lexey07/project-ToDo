# Factory Method

from abc import ABC, abstractmethod 
# Продукты
class Flowers(ABC):

    @abstractmethod
    def smell(self):
        pass

class Rose(Flowers):

    def smell(self):
        print("Пахнет розой")
class Daisies(Flowers):

    def smell(self):
        print("Пахнет ромашкой")

"""
'class FlowersFactory(ABC):' - создается абстрактная фабрика 'FlowersFactory'.
"""
# Создатель фабрики 
class FlowersFactory(ABC):

    """
    'def create_flowers(self) -> Flowers:' - объявляется метод 'create_flowers', который должен вернуть объект типа 'Flowers'.
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

# Конкретные фабрики
class RoseFactory(FlowersFactory):

    def create_flowers(self):
        return Rose()


class DaisiesFactory(FlowersFactory):

    def create_flowers(self):
        return Daisies()


# Использование
factory = RoseFactory()
factory.make_smell()

factory = DaisiesFactory()
factory.make_smell()