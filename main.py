from abc import ABC, abstractmethod
import math
import random


class Shape3D(ABC):
    @abstractmethod
    def surface_area(self):
        pass

    @abstractmethod
    def volume(self):
        pass


class Sphere(Shape3D):
    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3


class Cylinder(Shape3D):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * self.radius ** 2 * self.height


class Cube(Shape3D):
    def __init__(self, side):
        self.side = side

    def surface_area(self):
        return 6 * self.side ** 2

    def volume(self):
        return self.side ** 3


def generate_random_shape():
    shape_type = random.choice(["Sphere", "Cylinder", "Cube"])

    if shape_type == "Sphere":
        radius = random.randint(1, 10)
        return Sphere(radius)

    elif shape_type == "Cylinder":
        radius = random.randint(1, 10)
        height = random.randint(5, 20)
        return Cylinder(radius, height)

    else:
        side = random.randint(1, 10)
        return Cube(side)


shapes = []

for _ in range(10):
    shapes.append(generate_random_shape())

print("=" * 60)
print(f"{'Shape':<15}{'Surface Area':<20}{'Volume':<20}")
print("=" * 60)

for shape in shapes:
    shape_name = type(shape).__name__
    surface = shape.surface_area()
    volume = shape.volume()
    print(f"{shape_name:<15}{surface:<20.2f}{volume:<20.2f}")

