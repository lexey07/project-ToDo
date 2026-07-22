# Decorate

from abc import ABC, abstractmethod

class Room(ABC):

    @abstractmethod
    def cost(self):
        pass

class EmptyRoom(Room):
    
    def cost(self):
        return 1000

class RoomDecorate(Room):

    def  __init__(self, room):
        self.room = room

class TyaletDecorate(RoomDecorate):

    def cost(self):
        return self.room.cost() + 150

class Sofadecorate(RoomDecorate):

    def cost(self):
        return self.room.cost() + 200   

class TVDecorate(RoomDecorate):

    def cost(self):
        return self.room.cost() + 150
    
room = EmptyRoom()

room = TyaletDecorate(room)
room = TVDecorate(room)
room = Sofadecorate(room)

print(room.cost())