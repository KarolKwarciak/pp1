def f(array2D):
    index = 0
    for i in range(len(array2D[0])):
            column_sum = sum(row[i] for row in array2D)
            if column_sum == array2D[i][index]:
                index +=1
                return True
    return False
print(f([[3,7,2],[4,2,5],[5,2,1]]))