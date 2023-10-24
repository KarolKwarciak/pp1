rows = 7
columns = 7

number = 1
for i in range (1, rows + 1):
    for j in range (1, columns + 1):
        print(f' {number:2}',end='')
        number += 7
    print()
    number = i + 1

