arr = [2, 3, 2, 5, 8, 1, 9, 8]
a = []
for i in arr:
    if arr.count(i) == 1:
        a.append(i)
print(f"Arrays:", " ".join(map(str, arr)))
print(f"Unique elements:"," ".join(map(str,a)))