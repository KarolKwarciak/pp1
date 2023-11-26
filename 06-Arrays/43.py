def ordered_by_length(words):
    return sorted(words.split(), key = len)

word_list = "An apple a day keeps the doctor away"
result = ordered_by_length(word_list)
print(result)

    