def card_number():
    a = (input("Enter your 16-digits card number"))
    if len(a) == 16:
        masked_number = a[:2] +"*" * 12 + a[-4:]
        return masked_number
    else:
        return "Invalid card Number"




    