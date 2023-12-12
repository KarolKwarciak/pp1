def f(d,v):
    count_true = 0
    count_false = 0
    for key,value in d.items():
        if value == True:
            count_true += 1
        elif value == False:
            count_false += 1
    if v == True:
        return count_false
    elif v == False:
        return count_true
print(f({"a":True,"b":False,"c":True,"d":True}, False))