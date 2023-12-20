text = "I completely agree with you"
a = text.split()
b = list(map(lambda x:len(x),a))
print(b)