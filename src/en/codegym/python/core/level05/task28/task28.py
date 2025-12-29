# The Most Important Tuple

# Write a program that creates a tuple containing several nested tuples of integers.
# The program should use a for loop to find the maximum element in the nested tuples and print the result.

nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
max_el = nested_tuple[0][0]
for inner_tuple in nested_tuple:
    for el in inner_tuple:
        if el > max_el:
            max_el = el
print(max_el)


