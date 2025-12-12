# Access Denied

# Write a program that asks the user for a username and password.
# If the username is "admin" and the password is "1234", the program should print "Access Granted".
# Otherwise, the program should print "Access Denied".

username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin" and password == "1234":
    print("Access Granted")
else:
    print("Access Denied")
