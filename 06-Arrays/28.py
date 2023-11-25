def compare(arr1,arr2):
    a = " ".join(map(str, arr1))
    b = " ".join(map(str, arr2))
    if arr1 == arr2:
        return f"Array1: {a}\nArray2: {b}\ncomparison: True"
    else:
        return f"Array1: {a}\nArray2: {b}\ncomparison: False"
print(compare(["water","book","sky"],["water","book","sky"]))