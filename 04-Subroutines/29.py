def amount_to_pay(x):
    zloty5 = x//5
    remainder = x%5
    zloty2 = remainder//2
    remainder = remainder%2
    zloty1 = remainder
    return (zloty1 + zloty2 + zloty5)
e = amount_to_pay(2)
print(e)
    
    
#amount = int(input("Enter the amount in PLN: "))
#zloty5 = amount//5
#remainder = amount%5
#zloty2 = remainder//2
#remainder = remainder%2
#zloty1 = remainder
#print(f"The amount of PLN {zloty5} x 5pln, {zloty2} x 2pln, {zloty1} x 1pln in coins:")
