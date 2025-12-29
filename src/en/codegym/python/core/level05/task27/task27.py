# Sum of Tuples

# Write a program that creates a tuple containing several nested tuples of integers.
# The program should use a for loop to calculate the sum of all elements in the nested tuples and
# output the result.

nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
total = 0
for inner_tuple in nested_tuple:
    for number in inner_tuple:
        total += number
print(total)
