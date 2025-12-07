# Pythagorean Multiplication Table

# Write a program that asks the user for a number N and outputs an N x N multiplication table using nested loops.
# The program should only output the numbers of the table.
# Example:
# 1   2   3   ...
# 2   4   6   ...
# 3   6   9   ...
# ...


N = int(input("Insert N number: "))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(i * j, end='\t')
    print()
