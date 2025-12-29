# Adding an Element

# Write a program that creates a tuple with 5 elements entered by the user.
# Then the program should prompt the user for a new element and add it to the end of the tuple,
# creating a new tuple.
# The program should output the updated tuple.

my_tuple = ()
for i in range(5):
    element = input(f"Enter element {i+1}: ")
    my_tuple += (element,)
list_from_my_tuple = list(my_tuple)
element = input(f"Enter element to be added to the end : ")
list_from_my_tuple.append(element)
my_tuple = tuple(list_from_my_tuple)
print(my_tuple)
