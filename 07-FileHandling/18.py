
with open("30.txt") as file:
    file_2 = open("copy2.txt", "a")
    file_2.write(file.read())
    file_2.close()