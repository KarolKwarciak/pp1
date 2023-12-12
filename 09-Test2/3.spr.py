def f(c):
    count = 0
    for i  in c:
        if i.isdigit():
            count += int(i)
        else:
            count += 10
    return str(count)
print(f("2K9"))
print(f("234AJ7"))