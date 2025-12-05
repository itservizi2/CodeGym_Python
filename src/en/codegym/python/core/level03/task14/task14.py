# Indentation Overdrive
# Fix the indentation in the following code so that it correctly outputs the status
# depending on the number of points scored.

score = int(input("Enter the number of points scored: "))
if score >= 90:
    print("Excellent")
else:
    if score >= 75 and score < 90:
        print("Good")
    else:
        if score >= 50 and score < 75:
            print("Satisfactory")
        else:
            if score < 50:
                print("Unsatisfactory")
