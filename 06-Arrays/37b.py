def f(arr):
    for i in arr:
        a = max(arr)
        b = min(arr)
        return a - b
print(f([7,3,8,5,2]))