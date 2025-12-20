# Square list

# Write a program that creates a list of squares for numbers from -100 to 100. Use the list() function
# to create the list.
# Finally, print the resulting list on the screen.

square_list = list()
for numbers in range(-100,101):
    square_list.append(numbers * numbers)
print(square_list)



