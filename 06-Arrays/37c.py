def f(arr):
    n = len(arr)
    a = n//2
    if n%2 == 0:
        median = (arr[a] + arr[a-1])/2
    elif n%2 != 0:
        median = arr[a]
    return median
print(f([7,3,8,6,5,2]))