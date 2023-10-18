Number = str(input("Enter EAN-13 article number: "))
length = len(Number)
Poland = Number[0:3]
if length == 13 and Poland == "590":
    print("Article number is correct")
    print("Article manufactured in Poland")
elif length == 13 and Poland != "590":
    print("Article number is correct")
else:
    print("Article number is not correct")
