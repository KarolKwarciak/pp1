def f(a,b):
    result = []
    for i in range (a,b+1):
        if i % 2 == 0:
            result.append(str(i))
    return ",".join(result)

print(f(4,12))
    