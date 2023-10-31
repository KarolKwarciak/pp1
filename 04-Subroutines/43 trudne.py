def f(name):
    words = name.split()
    acronym = "".join(word[0] for word in words)
    return acronym
    



a = f("Jestem najlepszy ")
print(a)


def d(names):
    words = names.split()
    acronym = "".join(word[0] for word in words)
    return acronym


b = d("Jebac Disa")
print(b)