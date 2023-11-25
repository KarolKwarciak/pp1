arr = [15, 8, 31, 47, 2, 19]
index = 0
count = 0
while index < len(arr):
    count += arr[index]
    index += 1
    
print(f"Array: {arr}")
print(f"mean: {count/len(arr)}")