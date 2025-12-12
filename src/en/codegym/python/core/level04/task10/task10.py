# Leap Year

# Write a program that asks the user for a year and checks if it is a leap year.
# Use logical operators to check the conditions for a leap year.
# A leap year is divisible by 4, but not divisible by 100, except for years that are divisible by 400.

year = int(input("Enter year to be checked for being leap: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("year is leap ")
else:
    print("year is not leap")
