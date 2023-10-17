
height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))
print("Your BMI index: ",weight/height**2)
if 18 < weight/height**2 < 25:
    print ("Correct weight: True")
else:
    print("Correct weight: False")
