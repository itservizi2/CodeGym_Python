# Height in Feet and Inches
# Write a program that converts the user's height, given in centimeters, into feet and inches.
# The height value is given in the variable height_cm. One inch is equal to 2.54 cm, and one foot is equal to 12 inches.
# Your task is to calculate the number of complete feet in the given height and convert the remainder into inches.
# Display the result on the screen.

height_cm = float(input("Enter height in centimeters: "))

# Constants
cm_per_inch = 2.54
inch_per_foot = 12

# Write your code here
height_cm_convTO_inch = height_cm /cm_per_inch
height_full_feet = height_cm_convTO_inch // inch_per_foot
height_remaining_inches = height_cm_convTO_inch - (height_full_feet * inch_per_foot)
height_fullFeet_remainInches = f"{height_full_feet} Feet and {height_remaining_inches} Inches "
print(height_fullFeet_remainInches)

