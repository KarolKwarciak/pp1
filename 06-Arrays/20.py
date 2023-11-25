arr = [34,7,19,4,21,8]
while len(arr) > 0:
    count = 0
    for i in arr:  
        if i % 2 == 0:
            count += i
    print(count)
    break