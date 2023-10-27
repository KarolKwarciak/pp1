def f(number1,number2,operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "%":
        return number1 % number2
    elif operator == "*":
        return number1 * number2
    elif operator == "**":
        return number1 ** number2
a = f(6,3,"**")

print(a)

