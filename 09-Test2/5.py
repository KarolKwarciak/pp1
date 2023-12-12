#def f(first_letter,last_letter):
#    with open("data.txt", encoding = "utf-8") as file:
#        count = 0
#        for line in file:
#            line = line.strip()
#            if len(line) > 0 and first_letter.lower() == line[0].lower() and last_letter.lower() == line[-1].lower():
#                count += 1
#    return count
#print(f("w","d"))


import re

def f(first_letter, last_letter):
    count = 0

    with open("data.txt", encoding="utf-8") as file:
        for line in file:
            words = re.findall(r'\b' + re.escape(first_letter) + r'\w*' + re.escape(last_letter) + r'\b', line, re.IGNORECASE)
            count += len(words)

    return count

result = f("w", "d")
print(result)
