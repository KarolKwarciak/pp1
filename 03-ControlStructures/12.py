a = input("Enter first person name")
b = int(input("Enter first person age"))
c = input("Enter second person name")
d = int(input("Enter second person age"))
if b and d >= 18:
    print(f"Both {a} and {c} are adults")
elif b >= 18 and d < 18:
    print(f"{a} is adult but {c} is not")
elif b < 18 and d >=18:
    print(f"{c} is adult but {a} is not")
else:
    print(f"Both {a} and {c} are not adults")