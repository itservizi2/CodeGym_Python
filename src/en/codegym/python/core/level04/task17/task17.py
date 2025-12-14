# VAT
# Write a function calculate_total_cost(price, tax=0.2), which takes the price of the item and an optional
# tax parameter (default is 20%).
# The function should calculate and output the total cost of the item including tax.
# Then write a program that calls this function with various parameters.

def calculate_total_cost(price, tax=0.2):
    total = price * (1 + tax)
    print(f"Price: {price}, Tax: {tax * 100:.0f}%, Total cost: {total:.2f}")
    return total

print("Example 1: Default tax (20%)")
calculate_total_cost(100)

print("\nExample 2: Custom tax (10%)")
calculate_total_cost(50, 0.1)




