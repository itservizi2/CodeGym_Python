# Unique List.

# Write a program that creates a list of 10 elements, requested from the user.
# Then the program should create a set from the list elements to keep only unique elements and
# print the resulting set.

my_set = set()
my_list = []
for i in range(10):
    element = input(f"insert {i+1} elements : ")
    my_list.append(element)
my_set = set(my_list)
print(my_set)
