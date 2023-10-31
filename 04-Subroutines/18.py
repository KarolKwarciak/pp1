def f(numbers):
    a = " ".join(str(i) for i in range(1, numbers + 1))
    return a
    
a = f(15)
print(a)