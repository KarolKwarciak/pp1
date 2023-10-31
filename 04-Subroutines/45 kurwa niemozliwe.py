def f(expression):
    result = 0
    current_number = 0
    sign = 1  # 1 represents positive, -1 represents negative
    
    for char in expression:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char == '+':
            result += sign * current_number
            current_number = 0
            sign = 1
        elif char == '-':
            result += sign * current_number
            current_number = 0
            sign = -1
    
    # Add the last number in the expression
    result += sign * current_number
    
    return result

a = f("2 + 3")
print(a)  # Output: 5
