def occurs(number,array):
    for i in array:
        if i == number:
            return True
    return False
a = int(input("Enter your number"))
b = [15, 38, 7, 23, 14]
print(occurs(23,[15, 38, 7, 23, 14]))
if occurs(a,b):
    print(f"Number: {a}\nArray: {" ".join(map(str, b))}\nResult: number {a} apppears in the array")
else:
    print(f"Number: {a}\nArray: {" ".join(map(str, b))}\nResult: number {a} doesnt appear in the array")