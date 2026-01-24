# Packing

# Write a program that includes a dictionary, which includes a list, which includes a dictionary,
# which includes a list, which includes a string.

my_list_1 = ["apple", "banana", "cherry"]
my_dict_1 = {
    "fruits": my_list_1
}
my_list_2 = [my_dict_1]
my_dict_2 = {
    "nested": my_list_2
}
print(my_dict_2)
