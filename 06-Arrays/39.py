arr = [1,2,3,4,5,6,7]
odd_list = []
even_list = []
for i in arr:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(odd_list + even_list)
    