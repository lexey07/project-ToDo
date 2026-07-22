# Adapter

class Cat:

    def sound(self):
        print("MAY")

class CatAdapter:

    def __init__(self,cat):
        self.cat = cat
    
    def speak(self):
        self.cat.sound()
    
cat = Cat()
adapter = CatAdapter(cat)
adapter.speak()