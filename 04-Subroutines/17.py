def different(n1,n2,n3):
    if n1 != n2 != n3:
        return True
    else:
        return False
    
a = different(3,3,7)
print(a)



a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the third number"))
if a != b != c:
    print(f"Numbers {a},{b} and {c} are different")
else:
    print("At least two of those numbers are the same")