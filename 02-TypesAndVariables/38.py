phone_number = input("Enter phone number: ")
formatted_number = f"{phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:]}"
print(f"Phone number: {formatted_number}")
