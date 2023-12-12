def get_matrix(n):
        return [[i * n + j + 1 for j in range(n)] for i in range(n)]
matrix = (get_matrix(3))
for i in matrix:
    print(" ".join(map(str,i)))
