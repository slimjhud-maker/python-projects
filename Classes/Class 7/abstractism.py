from abc import ABC, abstractmethod,    astractmethod
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass
    @abstractmethod
    def change_bg(self):
        pass
    @abstractmethod
    def resize(self):
        pass

class Rectangle(Shape):
    @abstractmethod
    def draw(self):
        print("Drawing a rectangle")
    @abstractmethod
    def change_bg(self):
        print("Changing background of rectangle")
    @abstractmethod
    def resize(self):
        print("Resizing rectangle")

class Circle(Shape):
    @abstractmethod
    def draw(self):
        print("Drawing a circle")
    @abstractmethod
    def change_bg(self):
        print("Changing background of circle")
    @abstractmethod
    def resize(self):
        print("Resizing circle")

shape = Rectangle()
shape.draw()
shape.change_bg()
shape = Circle()
shape.draw()
shape.resize