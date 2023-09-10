def split_words_by_separator(words: list[str], separator: str):
    result = []
    for word in words:
        result.extend(word.split(separator))
    return [i for i in result if i]


print(split_words_by_separator(["one.two.three", "four.five", "six"], "."))
print(split_words_by_separator(["$easy$", "$problem$"], "$"))