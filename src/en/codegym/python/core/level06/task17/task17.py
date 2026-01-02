# Substring search.

# Write a program that takes a string and a substring from the user.
# The program should check if the substring is in the string using the in operator,
# find the first occurrence of the substring using the find() method, and
# count the number of occurrences of the substring using the count() method.
# The program should output all the results.

my_string = input("Enter a string: ")
my_substring = input("Enter a substring: ")
print(f" my substring exists in my string :", my_substring in my_string)
position = my_string.find(my_substring)
print(f" my substring position in my string :",position)
cnt = my_string.count(my_substring)
print(f" my substring count in my string :", cnt)
