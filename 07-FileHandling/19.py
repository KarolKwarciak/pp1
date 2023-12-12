
with open("30.txt") as file:
    file_2 = open("copy.txt", "a")
    for line in file:
        file_2.write(line)
    file_2.close()