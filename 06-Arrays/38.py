arr = [1,2,3,4,5,6,7]
list = []
a = (int(input("Enter your number: ")))
for i in arr:
    if i > a:
        list.append(i)
print(" ".join(map(str,list)))