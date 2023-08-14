def reverse_prefix(word: str, ch: str):
    if word.find(ch) == -1:
        return word
    prefix = word[:word.index(ch)+1]
    other_string = word[word.index(ch)+1:]
    return prefix[::-1] + other_string


print(reverse_prefix("abcdefd", "d"))
print(reverse_prefix("xyxzxe", "z"))
print(reverse_prefix("abcd", "z"))


