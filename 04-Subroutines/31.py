def f(x,y):
    count = 0
    for i in range(x,y):
        if i < 0 and i % 2 == 0:
            count += 1
    return count
a = f(-7,3)
print(a)