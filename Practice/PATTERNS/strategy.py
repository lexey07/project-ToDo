# Strategy

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def payment(self):
        pass

class Cash(Payment):

    def payment(self):
        print("Оплата наличными")

class Card(Payment):

    def payment(self):
        print("Оплата картой")

class SBP(Payment):

    def payment(self):
        print("Оплата СБП")

# Contex - основной объект, который ничего не знает о реализации, знает только о своей стратегии
class PaymentServies:

    def __init__(self, process):
        self.process = process

    def sent(self):
        self.process.payment()

payment = PaymentServies(Card())
payment.sent()
payment2 = PaymentServies(SBP())
payment2.sent()