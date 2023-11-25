filename = "filename.txt"

with open(filename, 'r') as file:
    for line in file:
        print(line, end="")
