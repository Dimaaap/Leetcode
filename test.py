def count_prefixes(words: list[str], s: str) -> int:
    counter = 0
    for word in words:
        if s.startswith(word):
            counter += 1
    return counter


print(count_prefixes(["a", "b", "c", "ab", "bc", "abc"], "abc"))
print(count_prefixes(["a", "a"], "aa"))