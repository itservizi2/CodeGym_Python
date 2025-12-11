# Comparing is very simple

# Write a program that asks the user for two floating-point numbers and compares them using an allowed
# error margin epsilon.
# Display the comparison result on the screen.

epsilon = 0.0001
float1 = float(input("INSERT A FLOAT NUMBER  "))
float2 = float(input("INSERT A FLOAT NUMBER  "))
if abs(float1 - float2) < epsilon:
    print("The 2 floats are equal")
else:
    print("The 2 floats are not equal")
