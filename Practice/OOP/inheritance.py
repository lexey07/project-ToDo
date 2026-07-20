from encapsulation import Car
"""
Наследование:

Классы могут передавать свои атрибуты и методы классам - потомкам.
"""
class Scooter(Car): # Наследуем все атрибуты и методы класса 'Car'

    """
    Чтобы все создалось корректно, необходимо вызвать метод 'super()'
    в методе '__init__' и через него заполнить атрибуты класса-родителя
    """
    def __init__(self, color, speed, model, name):
        super().__init__(color, speed)
        self._model = model
        self._name = name

    def new_sound_motor(self):
        print("БУМБУМБУМ")
    
    @property
    def model(self):
        return self._model
    
    @property
    def name(self):
        return self._name
    
    """
    '@name.setter' позволяет пользователям менять имя
    """
    @name.setter
    def name(self, new_name):
        if self._name != new_name:
            self._name = new_name
        return self._name

scooter1 = Scooter("Фиолетовый", 15, "7 series(2024)", "Baby")
scooter2 = Scooter("Розовый", 25, "8 series(2026)", "Batman")

scooter1.name = "Joker"

print(f"Наследование: {scooter1.model} {scooter1.color}")
scooter1.new_sound_motor()
scooter2.sound_motor()
