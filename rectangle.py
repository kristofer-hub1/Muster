from abc import ABC, abstractmethod

class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Width: {self.width}, Height: {self.height}"

class Square(Shape):
    def __init__(self, size):
        self.size = size

    @property
    def area(self):
        return self.size * self.size

    def __str__(self):
        return f"Size: {self.size}"

if __name__ == "__main__":
    r = Rectangle(2, 3)
    s = Square(5)

    print(r)
    print(s)
    print(f"Rectangle area: {r.area}")
    print(f"Square area: {s.area}")