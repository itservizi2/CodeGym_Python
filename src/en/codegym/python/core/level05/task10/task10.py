# Element Removal

# Write a program that creates a list of 5 elements, prompts the user for the index of an element to remove
# and removes the element at that index using the pop() method.
# The program should output the updated list and the removed element.
# If the index does not exist, the program should display a message about it.

my_list = [1,2,3,4,5]
el_index = int(input("insert index of element to pop : "))
if el_index in range(len(my_list)):
    popped_element = my_list.pop(el_index)
    print(f"popped element is : {popped_element}")
    print(my_list)
else:
    print("index not found")

