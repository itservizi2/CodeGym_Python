# Mix-Up

# Write a program that asks the user for an integer, a float, and a string.
# Then convert the integer to a float, the float to a string, and the string to an integer (if possible).
# Display the results of the conversions and their types.

int_input = int(input("Enter an integer: "))
float_input = float(input("Enter a float: "))
str_input = input("Enter a string: ")


int_to_float = float(int_input)
float_to_str = str(float_input)
str_to_int = int(str_input)

print(f"Integer to float: {int_to_float}, type: {type(int_to_float)}")
print(f"Float to string: {float_to_str}, type: {type(float_to_str)}")
print(f"String to integer: {str_to_int}, type: {type(str_to_int)}")
