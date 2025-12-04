# Squaring the Circle
# Write a program that asks the user for the radius of a circle (a float number), calculates its area,
# and prints the result.
# Use the float() function to convert the input. The formula for calculating the area of a circle is: 𝜋*r^2 (π≈3.14)
# Example:
# Enter the radius of the circle: 5
# Area of the circle: 78.5

print("Enter circle radius")
radius = float(input())
circle_area = radius * radius * 3.14
print("Area of the circle:", circle_area)
