from abc import ABC, abstractmethod

class Shaurma:

    def __init__(self):
        self.cucumber = None
        self.lavash = None
        self.cheese = None
        self.chicken = None

    def show(self):
        print(self.cucumber)
        print(self.lavash)
        print(self.cheese)
        print(self.chicken)

class ShaurmaBuilder(ABC):

    @abstractmethod
    def set_cucumber(self):
        pass

    @abstractmethod
    def set_lavash(self):
        pass

    @abstractmethod
    def set_cheese(self):
        pass
    
    @abstractmethod
    def set_chicken(self):
        pass

    @abstractmethod
    def build(self):
        pass

class ShaurmaBBQBuilder(ShaurmaBuilder):

    def __init__(self):
        self.shaurma = Shaurma()

    def set_cucumber(self):
        self.shaurma.cucumber = 'Соленные огурчики'

    def set_cheese(self):
        self.shaurma.cheese = 'Сыр российский'

    def set_lavash(self):
        self.shaurma.lavash = 'Лаваш черный'
    
    def set_chicken(self):
        self.shaurma.chicken = 'Петух' 
    
    def build(self):
        return self.shaurma

class ShaurmaClassikBuilder(ShaurmaBuilder):

    def __init__(self):
        self.shaurma = Shaurma()

    def set_cucumber(self):
        self.shaurma.cucumber = 'Огурчики обысные'

    def set_cheese(self):
        self.shaurma.cheese = 'Сыр пармезан'

    def set_lavash(self):
        self.shaurma.lavash = 'Лаваш белый'
    
    def set_chicken(self):
        self.shaurma.chicken = 'Курица' 
    
    def build(self):
        return self.shaurma
    
class Director:
    
    def __init__(self, builder):
        self.builder = builder
    
    def construct(self):

        self.builder.set_cucumber()
        self.builder.set_cheese()
        self.builder.set_lavash()
        self.builder.set_chicken()

        return self.builder.build()

shaurma_train = ShaurmaBBQBuilder()
director = Director(shaurma_train)

shaurma_tyalet = director.construct()

shaurma_tyalet.show()
