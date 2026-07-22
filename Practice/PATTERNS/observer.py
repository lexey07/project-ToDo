# Observer

from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def update(self):
        pass

class User(Observer):

    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(message)

class Channel:

    def __init__(self):
        self.subscribers = []
    
    def subscribe(self, observer):
        self.subscribers.append(observer) # Добавляем каждого пользователя в список

    def notify(self, message):
        for observer in self.subscribers: # <- Она означает пройдись по всем подписчикам и сообщи каждому об изменении
            observer.update(message)

    def upload_message(self, title):
        print(f"{title} ЙОУ")
        self.notify(title)
    
channel = Channel()

alexey = User("Alexey")
andrew = User("Andrew")

channel.subscribe(alexey)
channel.subscribe(andrew)

channel.upload_message("Новое уведомление!")