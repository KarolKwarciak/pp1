for i in range (1,31):

    if i % 3 == 0 and i % 5 == 0:
        print("Bingo!")
    elif i % 5 ==0:
        print("Five")
    elif i % 3 == 0:
        print("Three")
    else:
        print(i)



