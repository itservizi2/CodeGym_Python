# Tuple Grouping

# Write a program that creates a tuple of 6 elements requested from the user.
# Then the program should group them into 3 tuples of 2 elements each.
# Then combine the 1st and 3rd tuples and print the updated tuple on the screen.

my_tuple = ()
for i in range(6):
    element = input(f"Enter element {i + 1}: ")
    my_tuple += (element,)
list1 = list(my_tuple[0:2])
list2 = list(my_tuple[2:4])
list3 = list(my_tuple[4:6])
tuple1 = tuple(list1)
tuple2 = tuple(list2)
tuple3 = tuple(list3)
tuple_1_and_3 = tuple1  + tuple3
print(tuple_1_and_3)
