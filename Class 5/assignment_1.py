class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def honk(self):
        print("Car goes honk!")

class Bike(Vehicle):
    def kick_start(self):
        print("Bike kick-started!")


c = Car()
c.move()
c.honk()

b = Bike()
b.move()
b.kick_start()