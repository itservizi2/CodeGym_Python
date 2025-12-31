# Multiplicity

# Create an empty set.
# Request 5 numbers from the user sequentially.
# For each, create a separate set and add it to the initial one.
# Display the resulting set on the screen.


result_set = set()
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    temp_set = {num}
    result_set |= temp_set
print("Resulting set:", result_set)

