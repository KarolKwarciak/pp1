decimal = int(input("Enter decimal number"))
binary_number = ""

while decimal > 0:
    remainder = decimal % 2
    binary_number = str(remainder) + binary_number
    decimal //=2
   

print("Binary representation:", binary_number)
   
