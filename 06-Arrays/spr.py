def f(w):
    string = w
    list = []
    dlugosc = len(string)
    for i in string:
        list.append(i)

    string2 = ""

    for i in range (0,dlugosc):
        if i % 2 == 0:
            string2 = string2 + list[i] + "+"
        else:
            string2 = string2 + list[i] + "-"
    string2 = string2[:-1]

    return string2

print(f("abcdefgh"))

