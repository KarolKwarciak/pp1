arr = [-15, 8, -31, 47, -2, 19]
min_number = arr[0]
max_number = arr[1]
for i in arr:
    if i > max_number:
        max_number = i
    if i < min_number:
        min_number = i
print(max_number, min_number)