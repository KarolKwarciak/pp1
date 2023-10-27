def binary_number():
    a = input("Enter your binary number")
    if all(bit in "01" for bit in a):
       return True
    else: 
        return False
result = binary_number()
print(result)