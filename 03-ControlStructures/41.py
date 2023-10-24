
correct_pin = "0805"

for attempt in range(3):
    entered_pin = input("Enter your PIN code: ")
    
    if entered_pin == correct_pin:
        print("PIN code correct. Access granted!")
        break
    else:
        remaining_attempts = 3 - (attempt + 1)
        if remaining_attempts > 0:
            print(f"Incorrect PIN code. {remaining_attempts} attempts remaining.")
        else:
            print("Incorrect PIN code. Card blocked.")
