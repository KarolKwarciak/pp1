import re
text = "To be, or not to be, that is the question"
samo = "[aeiouy]"
vowels = re.findall(samo,text)
a = len(vowels)
print(a)
