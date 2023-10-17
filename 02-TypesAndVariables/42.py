def binary_to_decimal(binary):
    decimal = 0
    binary_digits = list(str(binary))  
    binary_digits.reverse()  
    
    for i in range(len(binary_digits)):
        decimal += int(binary_digits[i]) * (2 ** i)
    return decimal

def main():
    binary_number = input("Enter a 4-digit binary number: ")
    
    if len(binary_number) != 4 or not binary_number.isdigit() or any(digit not in '01' for digit in binary_number):
        print("Invalid input. Please enter a 4-digit binary number.")
    else:
        decimal_number = binary_to_decimal(binary_number)
        print("Decimal equivalent:", decimal_number)

if __name__ == "__main__":
    main()