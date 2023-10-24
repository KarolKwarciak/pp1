total_sum = 0
count = 0

while True:
    number = float(input("Enter number (or 0 to stop): "))
    if number == 0:
        break
    total_sum += number
    count += 1

if count > 0:
    average = total_sum / count
else:
    average = 0

print(f"RESULT: Quantity={count}, Sum={total_sum}, Mean={average}")
