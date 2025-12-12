class Animal:
    def __init__(self, nameX, colourX):
        self.name = nameX
        self.colour = colourX
        self.sound = input("What sound does your animal make? ")
        self.prey = input("What prey is your animal hunting? ")
    def __del__(self):
        print("Destructor was called to clean the RAM")
    def hunt(self):
        print("The", self.name, "is hunting the", self.prey)
    def make_sound(self):
        print("The", self.name, "is making a noise that is a", self.sound)

cat = Animal("Cat", "ginger")
print("This is a", cat.colour, cat.name)
cat.hunt()
cat.make_sound()
dog = Animal("Dog", "golden")
print("This is a", dog.colour, dog.name)
dog.hunt()
dog.make_sound()

