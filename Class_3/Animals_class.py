class Animal:
    def __init__(self, breedX, colourX):
        self.breed = breedX
        self.colour = colourX
        self.prey = input("What prey is your animal hunting? ")
    def hunt(self):
        print("The", self.breed, "is hunting the", self.prey)

lion = Animal("Lion", "Yellow")
lion.hunt()
orca = Animal("Orca", "Black and White")
orca.hunt()

