with open("30.txt") as file:
    lines = file.readlines()
    total_lines = len(lines)
    current_lines = 0
    lines_per_iteration = 5

    while current_lines < total_lines:
        for i in range (5):
            if current_lines < total_lines:
                print(lines[current_lines], end = "")
                current_lines += 1
        input("Press Enter to continue...")


