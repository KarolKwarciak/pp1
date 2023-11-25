file = open("movies.txt", "r")
count = 0
for line in file:
    count += 1
print(f"File Name: movies.txt")
print(f"Number of lines: {count}")