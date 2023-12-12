def f(player1, player2):
    count = 0
    counta = 0
    for i in player1:
        if i.isdigit():
            count += int(i)
        else:
            count += 10
    for i in player2:
        if i.isdigit():
            counta += int(i)
        else:
            counta += 10
    if count == counta:
        return True
    else:
        return False

print(f("AJ973", "AQT72"))  # Output: True
print(f("9532", "K8"))      # Output: False
