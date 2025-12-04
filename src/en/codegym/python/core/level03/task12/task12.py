# Grader
# Write a program that asks the user for the number of points scored and outputs their grade according to the
# following scale:
# 90 and above: "Excellent"
# 75-89: "Good"
# 50-74: "Satisfactory"
# Less than 50: "Unsatisfactory"
# Use the if, elif, else statements.


print("insert your grade")
grade = float(input())
if grade >= 90:
    print("Excellent")
elif 75 <= grade <= 89:
    print("Good")
elif 50 <= grade <= 74:
    print("Satisfactory")
else:
    print("Unsatisfactory")


