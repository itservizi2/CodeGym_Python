# From sep to end

# Write a program that prints numbers from 1 to 5 on one line, separating them with asterisks.
# Then the program should print the message "End of program." on the same line after all the numbers.
# Use the sep and end parameters in the print() function.


print(*range(1, 6), sep="*" , end = "End of program.")


