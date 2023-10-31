def f(n1,n2,n3):
    if n1 > n2 > n3:
        return(n1 - n3)
    elif n1 > n3 > n2:
        return(n1 - n2)
    elif n2 > n1 > n3:
        return(n2 - n3)
    elif n2 > n3 > n1:
        return(n2 - n1)
    elif n3 > n1 > n2:
        return(n3 - n2)
    else:
        return(n3 - n1)
a = f(7,4,9)
b = f(2,12,8)
print(a,b)
