import random
arr = [random.randrange(1,1000) for i in range(8)]

print("-" * 41)
print("|" + "|".join(f"{num:4}" for num in arr) + "|")
print("-" * 41)
