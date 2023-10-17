a = float(input("Enter the price"))
b = float(input("Enter the discount"))
c = a - (a * b)/100
d = (a * b)/100
print("Price with discount: ",round(c,2))
print("The discount: ",round(d,2))