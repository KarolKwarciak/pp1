def f(number,even = True):
    digit_sum = 0
    while number > 0:
        digit = number%10
        if (digit%2 == 0) == even:
            digit_sum = digit_sum + digit
        number = number// 10
    return digit_sum

print(f(3124, True))

