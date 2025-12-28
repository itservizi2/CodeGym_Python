# Tuple Index

# Write a program that creates a tuple of 5 elements entered by the user.
# Then the program should ask the user for the index of an element and output the value of the element at that index.
# If the index is out of bounds, the program should output an appropriate message.

my_tuple = ()
for i in range(5):
    element = input(f"Enter element {i+1}: ")
    my_tuple += (element,)
index = int(input("insert an index "))
if 0 <= index < len(my_tuple):
    print("Element at index", index, "is:", my_tuple[index])
else:
    print("Index out of range")


