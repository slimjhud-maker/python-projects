class Human:
    def __init__(self, nameX, ageX):
        self.name = nameX
        self.age = ageX
    def eat(self):
        print(self.name, "is eating a meal")

jhud = Human("Jhud", 12)
jhud.eat()
akash = Human("Akash", 10)
akash.eat()