file = open("50.txt", "a")
count = 1
while count < 51:
    file.write(str(f"\n{count}"))
    print()
    count += 1
file.close()