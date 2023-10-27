def f(palindrome):
    if palindrome[0:] == palindrome[::-1]:
        return True
    else:
        return False
a = f("radar")
print(a)