import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

area, peri = circle_stats(3)

print(f"Area: {area:.2f}  Circumference: {peri:.2f}")