science = input("Are you interested in computer science? (yes/no):").lower() == "yes"
games = input("Do you like playing computer games? (yes/no):").lower() == "yes"
Instagram = input("Do you have an Instagram account? (yes/no):").lower() == "yes"
if science:
    print("Interested in computer science: Yes")
else:
    print("Interested in computer science: No")
if games:
    print("Playing computer games: Yes")
else:
    print("Playing computer games: No")
if Instagram:
    print("Has an Instagram account: Yes")
else:
    print("Has an Instagram account: No")