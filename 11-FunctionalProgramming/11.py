distance = int(input("Enter your distance"))
hours = int(input("Enter your hours"))
minutes = int(input("Enter your minutes"))
speed = lambda a,b,c: a/(b + (c/60))
print(round(speed(distance,hours,minutes),1))