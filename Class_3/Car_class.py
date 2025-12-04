class Car:
    def __init__(self, carX):
        self.car = carX
        self.brand = input("What brand is your car? ")
        self.model = input("What model is your car? ")
        self.year = input("What year was your car made? ")
    def drive(self):
        print(self.car, "is driving down a road")
    def brake(self):
        print(self.car, "comes to a sudden stop")

car_1 = Car("Car 1")
car_1.drive()
car_1.brake()
car_2 = Car("Car 2")
car_2.drive()
car_2.brake()