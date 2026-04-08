from enum import Enum
from abc import ABC, abstractmethod


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class Specification(ABC):
    @abstractmethod
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(spec.is_satisfied(item) for spec in self.args)


class BetterFilter:
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    bf = BetterFilter()

    print("Green products:")
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(p.name)

    print("Large blue products:")
    large_blue = SizeSpecification(Size.LARGE) & ColorSpecification(Color.BLUE)
    for p in bf.filter(products, large_blue):
        print(p.name)