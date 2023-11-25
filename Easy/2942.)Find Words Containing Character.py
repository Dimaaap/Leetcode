def find_words_containing(words: list[str], x: str):
    ans = []
    for index, word in enumerate(words):
        if x in word:
            ans.append(index)
    return ans


print(find_words_containing(["leet", "code"], "e"))
print(find_words_containing(["abc", "bcd", "aaaa", "cbc"], "a"))
print(find_words_containing(["abc", "bcd", "aaaa", "cbc"], "z"))
