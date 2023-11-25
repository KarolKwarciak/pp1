import random
file = open("random.txt", "a")
count = 0
while count < 50:
    file.write(str(f"\n{random.randrange(100,1000)}"))
    count += 1
file.close()