def computegrade(score):
    if score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    else:
        return 'F'

while True:
    try:
        score = float(input("Enter score: "))
        if 0.0 <= score <= 1.0:
            grade = computegrade(score)
            print(grade)
            break
        else:
            print("Score out of range. Please enter a number between 0.0 and 1.0.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
