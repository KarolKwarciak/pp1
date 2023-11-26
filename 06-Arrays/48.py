def create_2d_arr(x,y):
    result = [[0 for i in range(y)] for i in range (x)]
    return result
a = create_2d_arr(3,5)
for i in a:
   print(i)
