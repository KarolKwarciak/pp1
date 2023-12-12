import re
def f(t):
        list = []
        a = re.findall("\d+",t)
        for i in a:
            list.append(int(i))
        return sum(list)
print(f("11 and 4 is 15"))
print(f("water12, and 3play is not 8"))
