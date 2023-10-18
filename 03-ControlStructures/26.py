speed_limit_min = 40
speed_limit_max = 140


car_speed = int(input("Enter your speed "))
if car_speed < speed_limit_min:
    print("Warning: invalid car speed!!")
elif car_speed > speed_limit_max:
    print("Warning: invalid car speed!!")
else:
    print("Speed is valid")