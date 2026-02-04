class Vehicle:
    def __init__(self):
        pass

    def move(self):
        print("The vehicle is moving.")



class Car(Vehicle):
    def __init__(self):
        super().__init__()

    def honk(self):
        print("Car goes honk!")



class Bike(Vehicle):
    def __init__(self):
        super().__init__()

    def kick_start(self):
        print("Bike kick-started!")



c = Car()
c.move()
c.honk()

b = Bike()
b.move()
b.kick_start()