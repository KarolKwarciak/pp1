arr = [1,2,3]
arr2 = [1,2,3,4,5,6,7,8]
arr3 = [4,5,6,7,8,9,20]
result = [str(i) for i in arr if i not in arr2]
if result:
    print(False)
else:
    print(True)