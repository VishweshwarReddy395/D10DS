# Create a function that returns both area and Circumference of a circle given its radius

import math

def circle(radius):

    area = round( math.pi * radius ** 2,2)
    circumference = round(2 * math.pi * radius,2)

    return area, circumference

a , c = circle(2)

print(f"Area of the circle is {a} and circumference of the circle is {c}")
