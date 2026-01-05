# Freezing

# Write a program that creates several frozenset objects from different iterable objects (list, string).
# The program should:
# Create a frozenset from a list.
# Create a frozenset from a string.
# Perform union, intersection, difference, and symmetric difference of two frozenset sets.
# Output the results of each operation.

my_list = [1, 2, 3, "hello", "world"]
my_string = "hello world! 2"
fset1 = frozenset(my_list)
fset2 = frozenset(my_string)
print(f"union is : ", fset1.union(fset2))
print(f"intersection is : ",fset1.intersection(fset2))
print(f"difference is : ",fset1.difference(fset2))
print(f"symmetric difference is : ",fset1.symmetric_difference(fset2))
