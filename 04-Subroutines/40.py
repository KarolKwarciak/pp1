def sum_repeated_digits(number):
    digit_counts = {}  
    total_sum = 0
    
    for digit in str(number):
        if digit in digit_counts:
            digit_counts[digit] += 1
        else:
            digit_counts[digit] = 1
    
    for digit, count in digit_counts.items():
        if count > 1:
            total_sum += int(digit) * count
    
    return total_sum

print(sum_repeated_digits(1027))    
print(sum_repeated_digits(230335))  
print(sum_repeated_digits(513553007))