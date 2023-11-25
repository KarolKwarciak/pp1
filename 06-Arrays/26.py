arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest_name = arr[0]
for i in arr:
    if len(i) > len(longest_name):
        longest_name = i
print(f"Names:", " ".join(map(str, arr)))
print(f"Longest name is: {longest_name}")
