def f(n):
    if n < 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)
a = f(9)
print(a)

















