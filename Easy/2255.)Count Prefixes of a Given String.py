def count_prefixes(words: list[str], s: str):
    counter = 0
    for i in words:
        if s.startswith(i):
            counter += 1
    return counter


print(count_prefixes(["a", "b", "c", "ab", "bc", "abc"], "abc"))
print(count_prefixes(["a", "a"], "aa"))
