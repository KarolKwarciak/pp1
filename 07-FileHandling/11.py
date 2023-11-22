file = open("numbers.txt", "r")
count  = 0
for line in file:
    count += int(line)
    print(line, end="")
print()
print(count)

file.close()