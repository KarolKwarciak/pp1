import random
def rand_elem(array):
    for i in array:
        return array[random.randrange(len(array))]
print(rand_elem([1,2,3,4,5,5,6,7,8,9]))