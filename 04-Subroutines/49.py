def f(dice):
    for i in dice:
            most_frequent = max(set(dice), key = dice.count)
            return most_frequent
        
a = f("5233165554211")
print(a)
