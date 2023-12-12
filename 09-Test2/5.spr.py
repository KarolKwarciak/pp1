def f(arr2D):
    count = 0
    index = 0
    for i in arr2D:
        if arr2D[index][1] == arr2D[index][0] **2:
            count += 1
        index += 1
    return count
print(f([[4,16],[3,9],[-3,9]]))
print(f([[2,3],[2,4],[3,7]]))
print(f([[2,3],[2,3],[2,3]]))
print(f([[1,1],[1,1],[1,3]]))
