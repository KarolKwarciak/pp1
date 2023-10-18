a = int(input("Enter current product price: "))
b = int(input("Previous product price: "))
c = a/b 
if b * 9/10 > a:
    print("Buy the product!")
    print("Product price reduced by", 100 - c*100,"%" )
else:
    print("Do not but the product yet!")
