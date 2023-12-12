def f(e):
    count = 0
    for operator in e:
        if operator == "+":
            count += 1
        elif operator == "-":
            count -= 1
    return count
print(f("+-+++-+---"))
print(f("+-+++++-"))