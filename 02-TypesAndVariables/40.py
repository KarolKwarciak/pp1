Credit_card_number = input("Credit card number: ")
formatted_number = f"{Credit_card_number[:4]} {Credit_card_number[4:8]} {Credit_card_number[8:12]} {Credit_card_number[12:]}"
print(f"Credit card number: {formatted_number}")
