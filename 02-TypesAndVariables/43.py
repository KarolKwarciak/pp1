name = input("Enter your name: ")

print("Numerical representation of each letter in your name:")
for char in name:
    numerical_representation = ord(char)
    print(f"Character '{char}' has numerical representation: {numerical_representation}")