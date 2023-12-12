def f(arr):
    count = 0
    for word in arr:
        if 4 <= len(word) <= 12 and all(i.isalnum() or i == '_' for i in word):
            count += 1
    return count

print(f(["uek", "water_7_x", "anna.may", "a_b_c_d_e_f"]))
