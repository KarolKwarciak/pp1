Time = input("Enter time (24-hour format): ")
hour = int(Time[0:2])
minutes = Time[3:5]

if hour < 12:
    print(f"The time is {hour}:{minutes} am")
elif hour == 12:
    print(f"The time is {hour}:{minutes} pm")
else:
    print(f"The time is {hour - 12}:{minutes} pm")
