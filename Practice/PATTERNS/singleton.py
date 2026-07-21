# Singleton

class Settings():

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            
        return cls._instance
    
    def __init__(self):
        print("iPhone")

s1 = Settings()
s2 = Settings()

print(s1 is s2)