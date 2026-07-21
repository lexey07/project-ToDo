# Facade

class AcceptOrder:

    def accept_order(self):
        print("Заказ принят!")
    
class DeliverCook:

    def deliver_cook(self):
        print("Заказ доставлен повару!")

class DishReady:
    
    def dish_ready(self):
        print("Блюдо готов!")
    
class PassOfficier:

    def pass_officier(self):
        print("Передано официанту!")

class RestorantFacade:

    def __init__(self):
        self.acceptorder = AcceptOrder()
        self.delivercook = DeliverCook()
        self.dishready = DishReady()
        self.passofficier = PassOfficier()

    def process(self):
        self.acceptorder.accept_order()
        self.delivercook.deliver_cook()
        self.dishready.dish_ready()
        self.passofficier.pass_officier()


restorant = RestorantFacade()
restorant.process()