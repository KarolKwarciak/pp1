name = input("Enter a name: ")

if name.lower().endswith('a'):
    print(f"{name} is likely a female name.")
else:
    print(f"{name} is not a female name.")