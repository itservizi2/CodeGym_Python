# Cold Keys

# Write a program that creates several frozenset objects and uses them as keys in a dictionary.
# The program should:
# Create two frozenset from lists.
# Create a dictionary where the keys are frozenset and the values are strings.
# Print the dictionary.

list1 = ['apple', 'banana', "strawberry"]
list2 = ['carrot', 'potato', "cabbage"]
fset1 = frozenset(list1)
fset2 = frozenset(list2)
my_dict = {
    fset1: 'fruit_group1',
    fset2: 'vegetable_group1'
}
print(my_dict)


