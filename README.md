# 3D Shape Modeling with Abstraction in Python

## Objective
This project demonstrates abstraction in Python using an abstract base class for 3D shapes. Different shape classes implement methods to calculate surface area and volume. The program randomly generates shape objects and displays their properties.

## Classes

### Shape3D
An abstract base class that defines the common interface for all 3D shapes.

**Methods:**
- `surface_area()` - returns the surface area of the shape
- `volume()` - returns the volume of the shape

### Sphere
Represents a sphere.

**Formula:**
- Surface Area = 4πr²
- Volume = (4/3)πr³

### Cylinder
Represents a cylinder.

**Formula:**
- Surface Area = 2πr(r + h)
- Volume = πr²h

### Cube
Represents a cube.

**Formula:**
- Surface Area = 6a²
- Volume = a³

## Features
- Uses abstraction with Python's `abc` module
- Demonstrates inheritance and polymorphism
- Generates 10 random 3D shape objects
- Calculates and displays surface area and volume for each object

## How to Run

1. Make sure Python is installed.
2. Open terminal in the project folder.
3. Run:

```bash
python main.py
