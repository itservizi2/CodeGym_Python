# Reverse Tuple

# Write a program that creates a tuple from an arbitrary number of elements input by the user.
# Then the program should output the tuple in reverse order using slicing.

elements = input("Enter elements separated by spaces: ")
if elements.strip() == "":
    my_tuple = ()
else:
    my_tuple = tuple(elements.split())
reversed_tuple = my_tuple[::-1]
print(reversed_tuple)
