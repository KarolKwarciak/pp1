file = open("third.txt","a")
count = 1
while count < 11:
    file.write(f"\n{count},{count**2},{count**3}")
    count += 1
file.close()
    