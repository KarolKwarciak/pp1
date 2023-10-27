def f(detector):
    count = 0
    max_people = 3
    for movement in detector:
        if movement == "+":
            count += 1
        elif movement == "-":
            count -= 1
        if count>= max_people:
            return True
    return False
a = f("++--+--++--+")
print(a)
        
