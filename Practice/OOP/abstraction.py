"""
Абстракция:

Упрощение класса до тех атрибутов и методов, которые нужны
именно в этом коде, не пытаясь описать его целиком и отбрасывая
всё всторостепенное.
"""

"""
Этот класс для общий для всех транспортов на колёсах.
"""
class Push():
    def move(self):
        print("Двигается")
    
class Wheels(Push):
    def __init__(self, speed, color, count):
        super().__init__()
        self._speed = speed
        self._color = color
        self._count = count

    @property
    def speed(self):
        return self._speed
    
    @property
    def color(self):
        return self._color
    
    @property
    def count(self):
        return self._count

wheels = Wheels(10, "Black", 4)

print(wheels._speed)
wheels.move()
    
