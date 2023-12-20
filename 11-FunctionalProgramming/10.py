distance = int(input("Enter your distance"))
hours = int(input("Emter your hours"))
minutes = int(input("Enter your minutes"))
def avg_speed(distance,hours,minutes):
    time = hours + (minutes/60)
    speed = round((distance/time),1)
    return speed
print(avg_speed(distance,hours,minutes))

