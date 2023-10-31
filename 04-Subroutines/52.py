def power(x,n):
    if n == 0:
        return 1
    elif n > 0:
        return x * power(x, n - 1)
    else:
        return 1/power(x, -n)
    
a = power(5,-3)
print(a)