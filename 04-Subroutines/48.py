def f(product_code):
    if len(product_code) != 4:
        return False
    
    sum = 0
    for i in range(0,3):
        sum += int(product_code[i])
    
    if int(product_code[3]) == sum % 7:
        return True
    else:
        return False
        
a = f("1082")
print(a)