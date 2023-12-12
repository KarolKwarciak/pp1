#def get_matrix(n):
#        return [[i * n + j + 1 for j in range(n)] for i in range(n)]
#matrix = (get_matrix(3))
#for i in matrix:
#    print(" ".join(map(str,i)))

#def get_matrix(n):
#        return [[i * n + j + 1 for j in range(5)] for i in range(2)]
#matrix = (get_matrix(5))
#for i in matrix:
#    print("".join(map(str,i)))


def get_matrix(n):
        return [[5 + j for j in range(4)] for i in range(1)]
matrix = (get_matrix(4))
for i in matrix:
    print(" ".join(map(str,i)))