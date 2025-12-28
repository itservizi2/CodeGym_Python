# Custom Tuple

# Write a program that creates a tuple from an arbitrary number of elements entered by the user.
# Then, the program should print the last element of the tuple.
# If the tuple is empty, the program should display a message about it.

elements = input("Enter elements separated by spaces: ")
if elements.strip() == "":
    my_tuple = ()
else:
    my_tuple = tuple(elements.split())
if not my_tuple:
    print("Tuple is empty")
else:
    print("Last element of tuple is:", my_tuple[-1])
