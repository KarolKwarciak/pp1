def f(arr):
    biggest_num = max(arr[0],arr[1])
    sec_biggest = min(arr[0],arr[1])
    
    for i in arr:
        if i > biggest_num:
            biggest_num = i
        elif i > sec_biggest:
            sec_biggest = i
    
    return sec_biggest
print(f([7,3,8,5,2]))
