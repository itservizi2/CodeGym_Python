# Counting Money

# Write a program that prompts the user for numbers and sums them until the user enters a negative number.
# Use a while loop and the break statement to stop input when a negative number is entered.

print("Enter positive numbers to sum, enter a negative one to stop")
total_sum = 0
while True:
    number = int(input("Enter a number: "))
    if number < 0:
        break
    total_sum += number
print("Total sum:", total_sum)

