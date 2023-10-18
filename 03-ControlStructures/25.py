Number = int(input("Number of the products purchased "))
price = int(input("Enter product price "))
if Number <= 2:
    print("Amount to pay: ",Number*price)
else:
    print("Amount to pay: ",(Number - 2) * price + Number*(price*1/4))