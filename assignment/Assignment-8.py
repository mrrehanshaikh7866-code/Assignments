#Create a program to calculate the area of different shapes. Implement a function
#calculate_area that can compute the area of a circle, a rectangle, and a triangle based on the provided
#arguments. Use function polymorphism to handle different shapes.
import math

def calculate_area(shape, *args):
    if shape.lower() == "circle":
        radius = args[0]
        return math.pi * radius * radius

    elif shape.lower() == "rectangle":
        length, width = args
        return length * width

    elif shape.lower() == "triangle":
        base, height = args
        return 0.5 * base * height

    else:
        return "Invalid shape"
# Input from the user
shape = input("Enter shape (circle, rectangle, triangle): ")

if shape.lower() == "circle":
    radius = float(input("Enter radius: "))
    area = calculate_area(shape, radius)

elif shape.lower() == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = calculate_area(shape, length, width)

elif shape.lower() == "triangle":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = calculate_area(shape, base, height)

else:
    area = calculate_area(shape)

print("Area:", area)