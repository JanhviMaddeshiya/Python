import math

def area_of_circle(radius):
    return math.pi * (radius ** 2)

radius = 9

area = area_of_circle(radius)
print("The area of the circle with radius", radius, "is:", area)