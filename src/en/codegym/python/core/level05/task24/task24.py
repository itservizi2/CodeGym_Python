# Negative Tuples

# Write a program that creates a tuple of 7 elements, requested from the user.
# Then, the program should display the third from the end and the penultimate element of the tuple
# using negative indices.

my_tuple = ()
for i in range(7):
    element = input(f"Enter element {i+1}: ")
    my_tuple += (element,)
print("Third from the end:", my_tuple[-3])
print("Penultimate element:", my_tuple[-2])


